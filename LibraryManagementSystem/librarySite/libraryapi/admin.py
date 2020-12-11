from django.contrib import admin
from .models import Author, Book, Series, Publisher, Person, Student, Professor, BookStatus, Location

# Register your models here.
admin.site.register(Book)
admin.site.register(Location)
admin.site.register(BookStatus)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Professor)
