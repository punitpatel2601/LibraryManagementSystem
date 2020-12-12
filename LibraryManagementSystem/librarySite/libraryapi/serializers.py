from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import *


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class BookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatus
        fields = ('available',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer('author')
    publisher = PublisherSerializer('publisher')
    '''
    book_available = BookAvailableSerializer('book_available')
    book_unavailable = BookUnavailableSerializer('book_unavailable')
    '''
    book_status = BookStatusSerializer('book_status')

    class Meta:
        model = Book
        fields = ('id', 'title', 'year', 'pages',
                  'description', 'copies', 'language', 'book_type', 'author', 'publisher', 'book_status',)


class SeriesSerializer(serializers.ModelSerializer):
    books = BookSerializer('books')

    class Meta:
        model = Series
        fields = ('series_name', 'no_books', 'books',)


class BooksWithdrawnSerializer(serializers.ModelSerializer):
    bookid = BookSerializer('bookid')

    class Meta:
        model = BooksWithdrawn
        fields = ('withdrawerid', 'bookid',)


class BooksRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksRequest
        fields = ('requestid', 'book_name', 'book_author', 'book_year',)


class OrderContentsSerializer(serializers.ModelSerializer):
    orderNo = OrderSerializer('orderNo')
    book = BookSerializer('book')

    class Meta:
        model = OrderContents
        fields = ('orderNo', 'book')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('ucid', 'name', 'books_withdrawn',)


class StudentSerializer(serializers.ModelSerializer):
    person = PersonSerializer("person")

    class Meta:
        model = Student
        fields = ("person", "major")


class ProfessorSerializer(serializers.ModelSerializer):
    person = PersonSerializer("person")

    class Meta:
        model = Professor
        fields = ("person", "years_taught")
