from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Types(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Element(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    types = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
