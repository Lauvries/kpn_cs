from django.shortcuts import render
from django.views import View
from .forms import CustomerForm

# Create your views here.


class LandingPage(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'jello/landingpage.html', {
            "form": form
        })

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'jello/landingpage.html', {
                "form": CustomerForm()
            })
        return render(request, 'jello/landingpage.html', {
            "form": form
        })
