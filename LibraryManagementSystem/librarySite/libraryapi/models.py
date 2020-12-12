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
    available = models.BooleanField(default=True, null=False)

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True)
    next_availability = models.CharField(max_length=25, blank=True)

    def update(self):
        self.available = False
        self.next_availability = "30 days"
        self.location = None

    def __str__(self):
        return "Available: " + str(self.available)


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

    def update_status(self, status):
        if status:
            loc = Location.objects.filter(id=0)
            self.book_status = BookStatus.objects.create(
                available=True, next_availability="", location=loc)
            self.book_status.save()
            self.save()
        else:
            self.book_status = BookStatus.objects.create(
                available=False, next_availability="30 Days", location=None)
            self.book_status.save()
            self.save()

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


class BooksWithdrawn(models.Model):
    withdrawerid = models.IntegerField()
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)

# Users/Admin


class BooksRequest(models.Model):
    requestid = models.IntegerField(null=True)
    book_name = models.CharField(max_length=50, null=False,)
    book_author = models.CharField(max_length=50, null=False)
    book_publisher = models.CharField(max_length=50, null=True, blank=True)
    book_year = models.IntegerField()
    book_language = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "Request from " + str(requestid)


class Order(models.Model):
    order_num = models.IntegerField(primary_key=True, unique=True)
    cost = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return order_num


class OrderContents(models.Model):
    orderNo = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return orderNo + book


class Person(models.Model):
    books_withdrawn = models.IntegerField(null=True)
    books_requested = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True, related_name="books_required")

    ucid = models.IntegerField(primary_key=True, unique=True)
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
