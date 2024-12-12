from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.ImageField(upload_to="category/", null=True, blank=True)
    
    # Shfaqja emrit ne vend te Category object tek admin
    def __str__(self):
        return f'{self.category_name}'

    
class Item(models.Model):
    item_name = models.CharField(max_length=100, null=True, blank=True)
    item_description = models.TextField(max_length=500, null=True, blank=True)
    item_image = models.ImageField(upload_to="item/", null=True, blank=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    # Fusha qe percakton lidhjen ndermjet dy class: ne kete rast nje element i perket nje kategorie
    # dhe nje categori ka disa elemente:  Many-To-One ose One-To-Many relation
    item_category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    # Lidhje te tjera jane: 
    # One-To-One: psh: nje user - nje profil perdoret fusha  OneToOneField
    # Modeli USer importohet nga django (ky eshte thjesh nje shembull)
    item_user = models.OneToOneField(User,on_delete=models.CASCADE,  null=True,blank=True)
    # Many-To-Many: psh: disa elemente kane disa ngjyra
   
    # Shfaqja emrit ne vend te Item object tek admin
    def __str__(self):
        return f'{self.item_name}'

class Contact(models.Model):
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_surname = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=500, null=True, blank=True)
    
def __str__(self):
        return f'{self.contact_name} {self.contact_surname}'


