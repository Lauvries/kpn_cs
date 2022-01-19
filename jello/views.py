from django.shortcuts import render
from django.views import View
from .forms import CustomerForm

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
