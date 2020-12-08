from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, SeriesSerializer, PublisherSerializer, CustomerSerializer, LocationSerializer, BookAvailableSerializer, BookUnavailableSerializer
from .models import Author, Location, Book, Available_Book, Series, Unavailable_Book, Publisher, Customer, Student, Professor

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class BookAvailableViewSet(viewsets.ModelViewSet):
    queryset = Available_Book.objects.all()
    serializer_class = BookAvailableSerializer

class BookUnavailableViewSet(viewsets.ModelViewSet):
    queryset = Unavailable_Book.objects.all()
    serializer_class = BookUnavailableSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

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
