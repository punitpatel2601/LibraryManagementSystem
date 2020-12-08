from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
