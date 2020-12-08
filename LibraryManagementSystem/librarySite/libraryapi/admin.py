from django.contrib import admin
from .models import Author, Book, Publisher, Customer, Student, Professor

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Customer)
admin.site.register(Student)
admin.site.register(Professor)
