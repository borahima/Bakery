from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
   categories = Category.objects.all()
   context = {"infoItems": Item, "infoCategories": categories}
   return render(request, "home.html",context)



def aboutus(request):
    categories = Category.objects.all()
    context = {"infoCategories": categories}
    return render(request, "aboutus.html",context)

def menu(request):
    categories = Category.objects.all()
    context = {"infoCategories": categories}
    return render(request, "menu.html",context)

def detailItems(request, id):
    categories = Category.objects.all()
    detail = Item.objects.get(pk=id)
    context = {"detail":detail, "infoCategories": categories}
    return render(request, "detailItems.html", context)

def category(request, id):
    categories = Category.objects.all()
    # Vetem kategoria
    detailCategory = Category.objects.get(pk=id)
    # Elementet qe i perkasin categorise
    itemsCat = Item.objects.filter(item_category=detailCategory)
    context = {"detailCategory":detailCategory, 
               "infoCategories": categories,
               "itemsCat":itemsCat}
    return render(request, "categories.html", context)


def contact(request):
    if request.method == "POST":
        emri = request.POST["firstName"]
        mbiemri = request.POST["lastName"]
        email = request.POST["email"]
        koment = request.POST["comment"]
        if emri == "" or mbiemri == "" or email == "" or koment == "":
            messages.error(request, "Fill the form")
        else:
            Contact(
                contact_name=emri,
                contact_surname=mbiemri,
                contact_email=email,
                contact_comment=koment,
            ).save()
            messages.success(request, "Thank you")
    return render(request, "contact.html")





