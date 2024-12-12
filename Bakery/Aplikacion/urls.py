from django.urls import path
from . import views


urlpatterns = [
path("", views.home, name="homePage"),
path("about/", views.aboutus, name="aboutusPage"),
path("contact/", views.contact, name="contactPage"),
path("menu/", views.menu, name="menuPage"),
path("detailItem/<id>", views.detailItems, name="detailItemPage"),
path("category/<id>", views.category, name="categoryPage"),

]