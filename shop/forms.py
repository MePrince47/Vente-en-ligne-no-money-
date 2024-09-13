# forms.py

from django import forms
from .models import Utilisateur
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'category', 'image', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})  # Ajoutez une classe CSS au champ image
        self.fields['image'].widget.attrs.update({'accept': 'images/*'})  # Acceptez uniquement les fichiers images

class InscriptionUtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'mot_de_passe']

class ConnexionForm(AuthenticationForm):
  class Meta:
        model = User 
        fields = ['email', 'password']