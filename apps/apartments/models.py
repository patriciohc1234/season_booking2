from django.db import models


class Apartment(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    rate = models.IntegerField()
    capacity = models.IntegerField()
    address = models.CharField(max_length=100, default=None)
    def __str__(self):
    	return '{}' .format(self.name)

class ApartmentImage(models.Model):
    imageFile = models.ImageField(upload_to='apartments')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, default=None)

