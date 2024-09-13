from django.urls import path
from shop.views import *

urlpatterns = [
    path('', acc, name='acc'),
    path('/home', index, name='home'),
    path('/home1', index1, name='home1'),
    path('/home2', index2, name='home2'),
    path('/home3', index3, name='home3'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation" ),
    path('register/',user_register_simple, name="user_register_simple"),
    path('login/', connexion, name="login"),
    path('profil/', profile, name="profil"),
    path('add_product/', add_product, name="add_product"),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/',deconnexion, name="deconnexion"),
    
]

