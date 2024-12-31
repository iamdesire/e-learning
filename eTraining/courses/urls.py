from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stripe-paiement", views.home_stripe,name="homeStripe"),

]