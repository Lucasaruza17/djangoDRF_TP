from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    category = models.ForeignKey(Category, related_name='games', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title