from django.db import models
from unicodedata import decimal


class Service(models.Model):
    nom=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=6)

class Reservation(models.Model):
    nom_client=models.CharField(max_length=100)
    nom_famille=models.CharField(max_length=100)
    num_phone=models.CharField(max_length=20)
    email=models.EmailField()
    service_choice=models.CharField(max_length=200)
    schedules_available=models.DateTimeField(auto_now=True)


class DemandePerso(models.Model):
       first_name=models.CharField(max_length=100)
       last_name=models.CharField(max_length=100)
       email=models.EmailField()
       phone=models.CharField(max_length=200)
       picture=models.ImageField(upload_to='hairstyles/')
       date_sent=models.DateTimeField(auto_now_add=True)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.email