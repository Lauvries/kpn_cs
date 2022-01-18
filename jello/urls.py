from django.urls import path
from jello import views

urlpatterns = [
    path('yello/', views.LandingPage.as_view())
]
