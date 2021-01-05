from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name= "Home"),
    path("signup",views.signup, name= "SignUp"),
    path("login",views.login, name= "Login"),
    path("allPlants",views.allplants, name= "AllPlants"),    
    path("addPlant",views.addplant, name= "AddPlant"),
    path("viewPlant",views.viewplant, name= "ViewPlant"),
    path("placeOrder",views.placeorder, name= "PlaceOrder"),
    path("viewOrder",views.vieworder, name= "ViewOrder"),
]