from django.db.models import fields
from rest_framework import serializers

from .models import Author, Book, Publisher


class BookSerializer(serializers.HyperlinkedModelSerializer):

    publisher_details = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='publisher_details')

    class Meta:
        model = Book
        fields = ('id', 'title', 'year', 'pages',
                  'description', 'copies', 'language', 'publisher_details')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('authorID', 'aName')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('publisherID', 'pName', 'pCountry', 'phone')
