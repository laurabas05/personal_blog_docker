from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=20)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name