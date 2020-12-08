from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, CustomerSerializer
from .models import Author, Book, Publisher, Customer, Student, Professor

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('id')
    serializer_class = PublisherSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
