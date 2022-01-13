from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Movie(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image    = models.ImageField()
    available= models.BooleanField(default=True)

    def __str__(self):
        return self.name