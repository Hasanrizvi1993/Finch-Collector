from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']