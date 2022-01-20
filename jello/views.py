from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CustomerForm
from .models import Customer, Product
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


class CreateCustomer(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'jello/create_customer.html', {
            "form": form
        })

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'jello/create_customer.html', {
                "form": CustomerForm()
            })
        return render(request, 'jello/create_customer.html', {
            "form": form
        })


class LandingPage(View):
    def get(self, request):
        return render(request, 'jello/landingpage.html')

    def post(self, request):
        query = request.POST
        qset = self.qqset(query['query'])
        has_no_customers = False
        if qset:
            qset = qset.values()
        else:
            has_no_customers = True
        return render(request, 'jello/landingpage.html', {
            "qset": qset,
            "has_no_customers": has_no_customers
        })

    def qqset(self, query):
        qset = Customer.objects.all().values("email", "mobile_number",
                                             "zipcode", "house_number", "id")

        if qset.filter(email=query):
            return(qset.filter(email=query))
        elif qset.filter(mobile_number=query):
            return(qset.filter(mobile_number=query))
        elif qset.filter(zipcode=query[:6]):
            qset = qset.filter(zipcode=query[:6])
            return(qset.filter(house_number=query[7:]))


class CustomerDetail(View):
    def get(self, request, id):
        specific_customer = get_object_or_404(Customer, id=id)
        customer_products = specific_customer.products.all()
        specific_customer_dict = specific_customer.__dict__
        unused_products = self.unused_products(specific_customer)

        return render(request, "jello/customer_detail.html", {
            "customer": specific_customer_dict,
            "customer_products": customer_products,
            "unused_products": unused_products
        })

    def unused_products(self, specific_customer):
        customer_products = specific_customer.products.all()
        all_products = Product.objects.all()

        unused_products = []
        for product in all_products:
            if product not in customer_products:
                unused_products.append(product)
        return unused_products


def update_customer_products(request):
    product_list = request.POST.getlist('product')
    customer_id = request.POST.get('customer_id')
    customer = Customer.objects.get(id=customer_id)
    all_products_qset = Product.objects.all()
    product_obj_list = []

    for product in product_list:
        product_obj_list.append(all_products_qset.get(name=product))

    customer.products.add(*product_obj_list)

    return HttpResponseRedirect(reverse("customer-detail", args=[customer_id]))
