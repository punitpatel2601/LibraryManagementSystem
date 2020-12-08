from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Author, Book, Publisher


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'year', 'pages',
                  'description', 'copies', 'language')


class AuthorSerializer(serializers.ModelSerializer):
    bookID = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Author
        fields = ('authorID', 'aName', 'bookID')


class PublisherSerializer(serializers.ModelSerializer):
    bookID = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Publisher
        fields = ('publisherID', 'pName', 'pCountry', 'phone', 'bookID')
