from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CustomerForm, ProductForm
from .models import Customer, Product
from django.http import HttpResponseRedirect
from django.urls import reverse


class CreateCustomer(View):
    def get(self, request):
        session = request.session  # gain access to session data
        # if data was saved to session by creating product during customer creation, use this data.
        if 'tempform' in session.keys():
            customer_form = CustomerForm(session['tempform'])
            return render(request, 'jello/create_customer.html', {
                "customer_form": customer_form
            })
        else:  # else just render an empty form
            customer_form = CustomerForm()
            return render(request, 'jello/create_customer.html', {
                "customer_form": customer_form
            })

    def post(self, request):
        # create a customerform instance with data provided by user
        customer_form = CustomerForm(request.POST)
        if 'create-customer' in request.POST:  # if the field create-customer is in the request, try and save it
            if customer_form.is_valid():
                customer_form.save()
                created_customer_id = Customer.objects.all().last().id
                try:  # if tempform exists, delete it from session on successfull save
                    del request.session['tempform']
                except KeyError:
                    pass
                # redirect to customer that's just been created
                return HttpResponseRedirect(reverse('customer-detail', args=[created_customer_id]))
            return render(request, 'jello/create_customer.html', {  # if form isn't valid, render the form with all previous data, and error messages
                "customer_form": customer_form
            })
        else:  # if there's no create-customer key in the request, this means the create product button was pressed
            session = request.session
            # save all entered data to session for later use.
            session['tempform'] = request.POST
            # redirect to create product page
            return HttpResponseRedirect(reverse('create-product'))


class LandingPage(View):
    def get(self, request):
        # simply render landingpage.html
        return render(request, 'jello/landingpage.html')

    def post(self, request):
        query = request.POST  # get search query
        # call qqset with query to search the DB
        qset = self.qqset(query['query'])
        # set has_no_customers to False (only load specific text when this is set to true)
        has_no_customers = False
        if qset:  # if qqset() returned anything
            qset = qset.values()  # set qset to equal those values, then pass that to the html page
        else:
            # if qqset() did not return anything, set has_no_customers to True, pass boolean to html page
            has_no_customers = True
        return render(request, 'jello/landingpage.html', {
            "qset": qset,
            "has_no_customers": has_no_customers
        })

    def qqset(self, query):
        qset = Customer.objects.all().values("email", "mobile_number",
                                             "zipcode", "house_number", "id")  # get from DB all customer values of specific rows
        # Filter email and mobile_number first, then zipcode + then house_number (I did not include suffix)
        if qset.filter(email=query):
            return(qset.filter(email=query))
        elif qset.filter(mobile_number=query):
            return(qset.filter(mobile_number=query))
        elif qset.filter(zipcode=query[:6]):
            qset = qset.filter(zipcode=query[:6])
            return(qset.filter(house_number=query[7:]))


class CustomerDetail(View):
    def get(self, request, id):
        specific_customer = get_object_or_404(
            Customer, id=id)  # if id exists -> object, else 404
        customer_products = specific_customer.products.all()  # create list of all products
        # create dict for easy iteraton in html from customer object
        specific_customer_dict = specific_customer.__dict__
        # call unused_products() with specific_customer to create list of unused products based on used products
        unused_products = self.unused_products(specific_customer)

        return render(request, "jello/customer_detail.html", {
            "customer": specific_customer_dict,
            "customer_products": customer_products,
            "unused_products": unused_products
        })

    def unused_products(self, specific_customer):
        # get all products customer currently has
        customer_products = specific_customer.products.all()
        all_products = Product.objects.all()  # get all products

        unused_products = [
            product for product in all_products if product not in customer_products]  # compare customer_products and all_products and list the difference

        return unused_products  # return said difference


class CreateProduct(View):
    def get(self, request):  # list all products and ProductForm
        products = Product.objects.all()  # get all products
        form = ProductForm()  # instantiate empty productform and pass it to html
        return render(request, 'jello/create_product.html', {
            "form": form,
            "products": products
        })

    def post(self, request):
        # fill a productform instance with info from user
        form = ProductForm(request.POST)
        products = Product.objects.all()  # get all products

        if form.is_valid():
            form.save()  # if valid, save
        else:  # rerender same page with entered info and errors
            return render(request, 'jello/create_product.html', {
                "form": form,
                "products": products
            })
        # redirect to same page with blank form
        return HttpResponseRedirect(reverse("create-product"))


def update_customer_products(request):
    # get a list of all product names checked by user
    product_list = request.POST.getlist('product')
    # get the customer ID the products are checked for
    customer_id = request.POST.get('customer_id')
    customer = Customer.objects.get(
        id=customer_id)  # get whole customer object
    all_products_qset = Product.objects.all()  # get a list of all product objects

    product_obj_list = [all_products_qset.get(
        name=product) for product in product_list]  # list all product objects that correspond to the product_list names

    # add all the product objects to the customer products (this saves automagically)
    customer.products.add(*product_obj_list)

    # show updated customer detail
    return HttpResponseRedirect(reverse("customer-detail", args=[customer_id]))
