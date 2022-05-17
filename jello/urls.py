from django.urls import path
from jello import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name="landing-page"),
    path('create-customer/',
         views.CreateCustomer.as_view(), name="create-customer"),
    path('create-product/',
         views.CreateProduct.as_view(), name="create-product"),
    path('add-products', views.update_customer_products, name="add-products"),
    path('<int:id>', views.CustomerDetail.as_view(), name="customer-detail")
]
