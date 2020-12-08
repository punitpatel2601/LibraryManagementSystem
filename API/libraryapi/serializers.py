from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Author, Book, Publisher, Customer, Student, Professor


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'phone')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'year', 'pages',
                  'description', 'copies', 'language')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer("customer")

    class Meta:
        model = Student
        fields = ("customer", "major")


class ProfessorSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer("customer")

    class Meta:
        model = Professor
        fields = ("customer", "years_taught")
