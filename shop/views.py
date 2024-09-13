from django.shortcuts import redirect, render
from .models import Product, Commande ,Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product  # Importez votre modèle Product
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth.models import User  #


@login_required(login_url="connexion")
def acc(request):
    donnees = Category.objects.all()
    return render(request, 'shop/home.html',{'donnees':donnees})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Notez l'utilisation de request.FILES pour gérer les fichiers
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la liste des produits après ajout
    else:
        form = ProductForm()
    
    return render(request, 'shop/add_product.html', {'form': form})




def deconnexion(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url="connexion")
def profile(request):
    donnees = Utilisateur.objects.all()

    return render(request, 'shop/profil_admin.html',{'donnees': donnees}) 



def connexion(request):
    erreur = ""
    donnees = Utilisateur.objects.all()

    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        erreur = "click"
        if request.method == 'POST':
            erreur = "vld"
            email = request.POST.get('email')
            password = request.POST['password']
            
            # Recherche de l'utilisateur dans la base de données
            utilisateur = authenticate(request, username=email, password=password)

            if utilisateur is not None:
                erreur = "Informations vld"
                # Récupérer l'adresse IP de l'utilisateur
                adresse_ip = request.META.get('REMOTE_ADDR', None)

                erreur = utilisateur.id
                # Connexion réussie
                auth.login(request, utilisateur)
                return redirect("home")
            else:
                erreur = "Veuillez entrer des informations valides"
                # Échec de la connexion
            
    else:
        form = ConnexionForm()

    return render(request, 'shop/connexion.html', {'form': form, 'erreur': erreur, 'donnees': donnees})



def user_register_simple(request):
    if request.method == 'POST':
        form = InscriptionUtilisateurForm(request.POST)
        if form.is_valid():
            # Sauvegarde du formulaire pour récupérer les données
            form.save()
            
            # Création de l'utilisateur Django
            username = form.cleaned_data['nom']  # Adapté à votre formulaire
            email = form.cleaned_data['email']  # Adapté à votre formulaire
            password = form.cleaned_data['mot_de_passe']  # Adapté à votre formulaire
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Redirection après l'inscription réussie
            return render(request, 'shop/connexion.html')  # Redirigez vers votre page de connexion
            
    else:
        form = InscriptionUtilisateurForm()
    
    return render(request, "shop/inscription_c_e.html", {'form': form})



@login_required(login_url="connexion")
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    
    # Filtrer par nom de produit si spécifié dans le formulaire de recherche
    if item_name and item_name != '':
        product_object = product_object.filter(title__icontains=item_name)
    
    # Filtrer également par catégorie "téléphone"
    category_name = 'Telephone'
    products_telephone = Product.objects.filter(category__name=category_name)

    category_p_name = 'Plomberie'
    products_Plomberie = Product.objects.filter(category__name=category_p_name)

    # Filtrer par catégorie "tv" pour la pagination
    category_tv_name = 'tv'
    products_tv = Product.objects.filter(category__name=category_tv_name)

    # Pagination pour les produits généraux
    paginator = Paginator(product_object, 4)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)

    # Pagination pour les produits de la catégorie "tv"
    paginator_tv = Paginator(products_tv, 4)
    page_number_tv = request.GET.get('page')
    products_tv = paginator_tv.get_page(page_number_tv)

    return render(request, 'shop/index.html', {
        'product_object': product_object,
        'products_telephone': products_telephone,
        'products_Plomberie': products_Plomberie,
        'products_tv': products_tv,  # Ajoutez cette variable au contexte
    })

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')


    return render(request, 'shop/checkout.html') 

def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})          



@login_required(login_url="connexion")
def index1(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    
    # Filtrer par nom de produit si spécifié dans le formulaire de recherche
    if item_name and item_name != '':
        product_object = product_object.filter(title__icontains=item_name)
    
    # Filtrer également par catégorie "téléphone"
    category_name = 'Telephone'
    products_telephone = Product.objects.filter(category__name=category_name)

    category_c_name = 'Construction'
    products_Construction = Product.objects.filter(category__name=category_c_name)


    # Filtrer par catégorie "tv" pour la pagination
    category_tv_name = 'tv'
    products_tv = Product.objects.filter(category__name=category_tv_name)

    # Pagination pour les produits généraux
    paginator = Paginator(product_object, 4)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)

    # Pagination pour les produits de la catégorie "tv"
    paginator_tv = Paginator(products_tv, 4)
    page_number_tv = request.GET.get('page')
    products_tv = paginator_tv.get_page(page_number_tv)

    return render(request, 'shop/index1.html', {
        'product_object': product_object,
        'products_Construction': products_Construction,
        'products_telephone': products_telephone,
        'products_tv': products_tv,  # Ajoutez cette variable au contexte
    })


@login_required(login_url="connexion")
def index2(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    
    # Filtrer par nom de produit si spécifié dans le formulaire de recherche
    if item_name and item_name != '':
        product_object = product_object.filter(title__icontains=item_name)
    
    # Filtrer également par catégorie "téléphone"
    category_name = 'Telephone'
    products_telephone = Product.objects.filter(category__name=category_name)

    category_L_name = 'Location'
    products_Location = Product.objects.filter(category__name=category_L_name)

    # Filtrer par catégorie "tv" pour la pagination
    category_tv_name = 'tv'
    products_tv = Product.objects.filter(category__name=category_tv_name)

    # Pagination pour les produits généraux
    paginator = Paginator(product_object, 4)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)

    # Pagination pour les produits de la catégorie "tv"
    paginator_tv = Paginator(products_tv, 4)
    page_number_tv = request.GET.get('page')
    products_tv = paginator_tv.get_page(page_number_tv)

    return render(request, 'shop/index2.html', {
        'product_object': product_object,
        'products_telephone': products_telephone,
        'products_Location': products_Location,
        'products_tv': products_tv,  # Ajoutez cette variable au contexte
    })


@login_required(login_url="connexion")
def index3(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    
    # Filtrer par nom de produit si spécifié dans le formulaire de recherche
    if item_name and item_name != '':
        product_object = product_object.filter(title__icontains=item_name)
    
    # Filtrer également par catégorie "téléphone"
    category_name = 'Telephone'
    products_telephone = Product.objects.filter(category__name=category_name)

    category_L_name = 'Location'
    products_Location = Product.objects.filter(category__name=category_L_name)

    # Filtrer par catégorie "tv" pour la pagination
    category_tv_name = 'tv'
    products_tv = Product.objects.filter(category__name=category_tv_name)

    # Pagination pour les produits généraux
    paginator = Paginator(product_object, 4)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)

    # Pagination pour les produits de la catégorie "tv"
    paginator_tv = Paginator(products_tv, 4)
    page_number_tv = request.GET.get('page')
    products_tv = paginator_tv.get_page(page_number_tv)

    return render(request, 'shop/index3.html', {
        'product_object': product_object,
        'products_telephone': products_telephone,
        'products_Location': products_Location,
        'products_tv': products_tv,  # Ajoutez cette variable au contexte
    })