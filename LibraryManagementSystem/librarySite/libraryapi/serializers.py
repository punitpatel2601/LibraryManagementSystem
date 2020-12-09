from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Author, Location, Book, Available_Book, Unavailable_Book, Series, Publisher, Person, Student, Professor


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
        fields = ('next_availability', 'book')


class SeriesSerializer(serializers.ModelSerializer):
    books = BookSerializer('books')

    class Meta:
        model = Series
        fields = ('series_name', 'no_books', 'books')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


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


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Person
        fields = ['ucid', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def save(self):
            Person = Person(
                ucid=self.validated_data['ucid']
            )
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

            Person.set_password[password]
            Person.save()
            return Person
