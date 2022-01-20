from django.urls import path
from jello import views

urlpatterns = [
    path('jello/', views.LandingPage.as_view(), name="landing-page"),
    path('jello/create-customer/',
         views.CreateCustomer.as_view(), name="create-customer"),
    path('jello/<int:id>', views.CustomerDetail.as_view(), name="customer-detail")
]
