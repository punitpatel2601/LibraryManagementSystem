from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    description = models.CharField(max_length=500)
    copies = models.IntegerField()
    language = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title + " " + str(self.year) + " " + self.language
