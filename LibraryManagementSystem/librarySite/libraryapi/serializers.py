from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Author, Location, Book, Available_Book, Unavailable_Book, Series, Publisher, Customer, Student, Professor

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'phone')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer('author')
    publisher = PublisherSerializer('publisher')

    class Meta:
        model = Book
        fields = ('id', 'title', 'year', 'pages',
                  'description', 'copies', 'language', 'book_type', 'author', 'publisher')


class BookAvailableSerializer(serializers.ModelSerializer):
    book = BookSerializer('book')
    location = LocationSerializer('location')

    class Meta:
        model = Available_Book
        fields = ('book', 'location')


class BookUnavailableSerializer(serializers.ModelSerializer):
    book = BookSerializer('book')

    class Meta:
        model = Unavailable_Book
        fields = ('book', 'next_availability')


class SeriesSerializer(serializers.ModelSerializer):
    books = BookSerializer('books')

    class Meta:
        model = Series
        fields = ('series_name', 'no_books', 'books')


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
