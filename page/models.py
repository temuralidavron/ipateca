from django.db import models

# Create your models here.


class House(models.Model):
    ipateca = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()


    def __str__(self):
        return self.ipateca

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

