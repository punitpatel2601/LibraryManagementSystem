from django.db import models

from django.contrib.auth.models import User


# Books

class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " @ ID = " + str(self.id)


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + " @ ID = " + str(self.id)


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    description = models.CharField(max_length=500)
    copies = models.IntegerField()
    language = models.CharField(max_length=10)

    author = models.ForeignKey(Author, default=0, on_delete=models.SET_DEFAULT)
    publisher = models.ForeignKey(
        Publisher, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title


# Users/Admin

class Customer(models.Model):

    books_withdrawn = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, related_name="books_with")
    books_requested = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, related_name="books_req")
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    ucid = models.IntegerField(primary_key=True)
    faculty = models.CharField(max_length=25)

    def __str__(self):
        return str(self.username) + " @UCID = " + str(self.ucid)


class Student(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    major = models.CharField(max_length=25)

    def __str__(self):
        return str(self.customer) + " Major: " + self.major


class Professor(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    years_taught = models.IntegerField

    def __str__(self):
        return str(self.customer) + " Years Taught: " + str(self.years_taught)
