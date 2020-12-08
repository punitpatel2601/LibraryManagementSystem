from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer, BookSerializer, SeriesSerializer, PublisherSerializer, PersonSerializer, LocationSerializer, BookAvailableSerializer, BookUnavailableSerializer, StudentSerializer, ProfessorSerializer
from .models import Author, Location, Book, Available_Book, Series, Unavailable_Book, Publisher, Person, Student, Professor

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class BookAvailableViewSet(viewsets.ModelViewSet):
    queryset = Available_Book.objects.all()
    serializer_class = BookAvailableSerializer

class BookUnavailableViewSet(viewsets.ModelViewSet):
    queryset = Unavailable_Book.objects.all()
    serializer_class = BookUnavailableSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('id')
    serializer_class = PublisherSerializer



class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()
