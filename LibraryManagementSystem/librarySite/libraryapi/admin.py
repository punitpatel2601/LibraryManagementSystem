from django.contrib import admin
from .models import Author, Book, Series, Publisher, Person, Student, Professor, Available_Book, Unavailable_Book, Location

# Register your models here.
admin.site.register(Book)
admin.site.register(Location)
admin.site.register(Available_Book)
admin.site.register(Unavailable_Book)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Professor)
