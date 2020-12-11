from django.db import models

# Books


class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " @ ID = " + str(self.id)


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + " @ ID = " + str(self.id)


class Location(models.Model):
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    contact_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.address


class BookStatus(models.Model):
    available = models.BooleanField(default=True, primary_key=True, null=False)

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True)
    next_availability = models.CharField(max_length=25, blank=True)

    def update(self):
        available = False
        next_availability = "30 days"
        location = None


'''
class Available_Book(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Unavailable_Book(models.Model):
    next_availability = models.CharField(max_length=25)
'''


class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    description = models.CharField(max_length=500)
    copies = models.IntegerField()
    language = models.CharField(max_length=10)

    OTHER = 'OTHER'
    BIOGRAPHY = 'BIOGRAPHY'
    FICTION = 'FICTION'
    NONFICTION = 'NON-FICTION'

    BOOK_TYPES = ((OTHER, 'Other'),
                  (BIOGRAPHY, 'Biography'),
                  (FICTION, 'Fiction'),
                  (NONFICTION, 'Non-Fiction'))

    book_type = models.CharField(
        max_length=25, choices=BOOK_TYPES, default=OTHER)
    author = models.ForeignKey(Author, default=0, on_delete=models.SET_DEFAULT)
    publisher = models.ForeignKey(
        Publisher, default=0, on_delete=models.SET_DEFAULT)

    book_status = models.ForeignKey(
        BookStatus, on_delete=models.CASCADE, null=True)

    '''
    book_available = models.ForeignKey(
        Available_Book, on_delete=models.CASCADE, blank=True, null=True)
    book_unavailable = models.ForeignKey(
        Unavailable_Book, on_delete=models.CASCADE, blank=True, null=True)
    '''

    def __str__(self):
        return self.title


class Series(models.Model):
    series_name = models.CharField(max_length=50)
    no_books = models.IntegerField()
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.series_name


# Users/Admin

class Person(models.Model):

    books_withdrawn = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True, related_name="books_with")
    books_requested = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True, related_name="books_req")

    ucid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

    OTHER = 'OTHER'
    SCIENCES = 'SCI'
    ENGG = 'ENGG'
    MATH = 'MATH'
    ART = 'ART'
    IT = 'IT'

    FACULTYCHOICES = ((OTHER, 'Other'),
                      (SCIENCES, 'Sciences'),
                      (ENGG, 'Engineering'),
                      (MATH, 'Mathematics'),
                      (ART, 'Arts'),
                      (IT, 'Information Technology'))

    faculty = models.CharField(
        max_length=25, choices=FACULTYCHOICES, default=OTHER)

    def __str__(self):
        return str(self.ucid)


class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    major = models.CharField(max_length=25)

    def __str__(self):
        return str(self.person) + " Major: " + self.major


class Professor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    years_taught = models.IntegerField

    def __str__(self):
        return str(self.person) + " Years Taught: " + str(self.years_taught)
