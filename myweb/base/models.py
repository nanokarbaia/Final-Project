from django.db import models

# Create your models here.

class Pict(models.Model):
    picture=models.CharField(max_length=400)
    # name=models.CharField(max_length=200)
    # author=models.CharField(max_length=200)
    # description=models.TextField(max_length=500)
    # content=models.CharField(max_length=200)

    # def __str__(self):
    #     return f"{self.name} _ {self.author}"