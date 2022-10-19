from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField()
    premium = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        unique_together = ("longitude", "latitude")

    def __str__(self):
        return f"lat : {self.longitude}, long: {self.latitude}"


class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='Price')

    def __str__(self):
        return f"{self.name} ({self.address})"


class Price(models.Model):
    value = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product.name}: {self.value} Ar at {self.store.name}"