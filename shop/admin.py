from django.contrib import admin
from .models import Category, Product, Commande

from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')  # Champs à afficher dans la liste
    search_fields = ('nom', 'prenom', 'email')  # Champs utilisés pour la recherche
    list_filter = ('nom', 'email')  # Filtres latéraux pour filtrer par nom ou email
# Register your models here.
admin.site.site_header = "E-commerce"
admin.site.site_title = "SBC shop"
admin.site.index_title = "Manageur"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',) 
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom','email','address', 'ville', 'pays','total', 'date_commande', )

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
