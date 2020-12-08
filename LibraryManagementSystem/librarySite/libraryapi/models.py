from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    description = models.CharField(max_length=500)
    copies = models.IntegerField()
    language = models.CharField(max_length=10)
    pubID = models.IntegerField

    def __str__(self):
        return self.title


class Author(models.Model):
    authorID = models.IntegerField(primary_key=True, unique=True)
    aName = models.CharField(max_length=100)

    def __str__(self):
        return self.aName + " @ ID = " + str(self.authorID)


class Publisher(models.Model):
    publisherID = models.IntegerField(primary_key=True, unique=True)
    pName = models.CharField(max_length=30)
    pCountry = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.pName + " @ ID = " + str(self.publisherID)
