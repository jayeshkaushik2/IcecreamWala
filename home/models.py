from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=20)
    massage = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Search(models.Model):
    icecream_name = models.CharField(max_length=50)
    date = models.DateField()
    def __str__(self):
        return self.icecream_name

class Icecream_item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    flavour = models.CharField(max_length=50)
    image = models.ImageField(upload_to="icecream_image")
    def get_id(self):
        return self.id

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    item_id = models.IntegerField()
    def __str__(self):
        return self.name

class Bought_items(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)



class Address(models.Model):
    item_id = models.ForeignKey(Bought_items, default=True, on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    fullname = models.CharField(max_length=120)
    mobilenumber = models.CharField(max_length=120)
    pincode = models.CharField(max_length=120)
    home_address = models.CharField(max_length=120)
    village = models.CharField(max_length=120)
    landmark = models.CharField(max_length=120)
    town_city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.fullname
