from django.db import models

# Create your models here.


# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class User(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=15)





