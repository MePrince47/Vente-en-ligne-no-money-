from django.db import models
from django.db.models.fields.related import ForeignKey


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.email})"


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/', default='images/default.png')  # Définissez le répertoire d'upload
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom   

   