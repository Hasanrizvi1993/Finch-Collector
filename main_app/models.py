from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#carmodel models
class CarType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Car(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cartypes = models.ManyToManyField(CarType)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

