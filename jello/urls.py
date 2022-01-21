from django.urls import path
from jello import views

urlpatterns = [
    path('jello/', views.LandingPage.as_view(), name="landing-page"),
    path('jello/create-customer/',
         views.CreateCustomer.as_view(), name="create-customer"),
    path('jello/create-product/',
         views.CreateProduct.as_view(), name="create-product"),
    path('jello/add-products', views.update_customer_products, name="add-products"),
    path('jello/<int:id>', views.CustomerDetail.as_view(), name="customer-detail")
]
