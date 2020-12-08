from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer
from .models import Author, Book, Publisher

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('authorID')
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('publisherID')
    serializer_class = PublisherSerializer
