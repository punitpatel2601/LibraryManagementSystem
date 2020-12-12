from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .serializers import *
from .models import *
from .forms import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class BookStatusViewSet(viewsets.ModelViewSet):
    queryset = BookStatus.objects.all()
    serializer_class = BookStatusSerializer


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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderContentViewSet(viewsets.ModelViewSet):
    queryset = OrderContents.objects.all()
    serializer_class = OrderContentsSerializer


class BooksWithdrawnViewSet(viewsets.ModelViewSet):
    queryset = BooksWithdrawn.objects.all().order_by('withdrawerid')
    serializer_class = BooksWithdrawnSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()


class RequestNewBookViewSet(viewsets.ModelViewSet):
    queryset = BooksRequest.objects.all()
    serializer_class = BooksRequestSerializer


def index(request):
    return render(request, 'api/index.html')


def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            ucid = form.cleaned_data['ucid']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            faculty = form.cleaned_data['faculty']

            print(ucid)
            print(name)
            print(password)
            print(password2)

            if(password != password2):
                return HttpResponseRedirect('/register/')

            user_instance = Person.objects.create(
                ucid=ucid, password=password, name=name, faculty=faculty)
            user_instance.save()

            return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()

    return render(request, 'api/register.html', {'form': form})


person = None


def redirect_home(request):
    if person is None:
        return index(request)
    return HttpResponseRedirect('/welcome/')


def login(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            ucid = form.cleaned_data['ucid']
            password = form.cleaned_data['password']

            person_list = Person.objects.all()
            found = False
            for p in person_list:
                if (p.ucid == ucid and p.password == password):
                    found = True
                    global person
                    person = p
                    break

            if (found == False):
                return HttpResponseRedirect('notSuccess/')

            return HttpResponseRedirect('/welcome/')
    else:
        form = LoginForm()

    return render(request, 'api/login.html', {'form': form})


def welcome(request):
    if person is None:
        return index(request)

    print(person.ucid)
    return render(request, 'api/welcome.html')


def unsuccessful(request):
    return render(request, 'api/notSuccess.html')


def display_books(request):
    if person is None:
        return index(request)

    books = Book.objects.all()
    form = BorrowBookForm()
    return render(request, 'api/viewBooks.html', {'books': books, 'form': form})


def borrow_book(request):
    if person is None:
        return index(request)

    print(str(person.ucid) + " Borrow")
    if(request.method == 'POST'):
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            query_id = form.cleaned_data['book_id']

            book = Book.objects.filter(id=query_id)

            if book:
                b = book[0]
                status = b.book_status

                if status.available is True:

                    # decrease the number of copies available
                    book[0].copies -= 1
                    book[0].save()

                    # if no more copies available set the book status as unavailable
                    if book[0].copies == 0:
                        book[0].update_status(False)
                        book[0].save()

                    bookW = BooksWithdrawn.objects.create(
                        withdrawerid=person.ucid, bookid=book[0])

                    person.books_withdrawn += 1
                    person.save()

                    return render(request, 'api/borrowSuccess.html', {'book': b})

            return HttpResponseRedirect('/welcome/')
    else:
        form = BorrowBookForm()
        return HttpResponseRedirect('selectBook/', {'form', form})


def search_book(request):
    if person is None:
        return index(request)

    if (request.method == 'GET'):
        form = SearchBookForm()
        return render(request, 'api/searchBooks.html', {'form': form})
    else:
        form = SearchBookForm(request.POST)
        if form.is_valid():
            query_name = form.cleaned_data['book_name']
            query_id = form.cleaned_data['book_id']
            series_name = form.cleaned_data['series_name']

            if(query_id == None and query_name == None and series_name == None):
                return HttpResponseRedirect('/searchBook/')

            if (query_id):
                books = Book.objects.filter(id=query_id)
            elif (query_name):
                books = Book.objects.filter(title=query_name)
            else:
                # TODO search by series name
                books = []

            return render(request, 'api/viewBooks.html', {'books': books, 'form': BorrowBookForm()})
        else:
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)


def display_user_info(request):
    if person is None:
        return index(request)
    my_books = get_user_withdrawn_books()
    return render(request, 'api/userInfo.html', {'person': person, 'books': my_books})


def return_book(request):
    if person is None:
        return index('GET')

    if request.method == 'GET':
        form = ReturnBookForm()
        my_books = get_user_withdrawn_books()
        return render(request, 'api/returnBooks.html', {'books': my_books, 'form': form})
    else:
        form = ReturnBookForm(request.POST)

        if form.is_valid():
            query_id = form.cleaned_data['book_id']

            if (query_id == None):
                return HttpResponseRedirect('/returnBook/')

            returned_book = None
            for b in get_user_withdrawn_books():
                if b.id == query_id:
                    returned_book = b

            if returned_book is None:
                return HttpResponseRedirect('/returnBook/')

            returned_book.copies += 1
            if returned_book.book_status.available == False:
                returned_book.update_status(True)

            w = find_withdrawn_from_book_id(query_id)
            w.delete()

        else:
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)


def find_withdrawn_from_book_id(bookid):
    if person is None:
        return index('GET')

    all_withdrawn = BooksWithdrawn.objects.all()

    if all_withdrawn:
        for w in all_withdrawn:
            if w.withdrawerid == person.ucid and w.bookid.id == bookid:
                return w

    return None


def get_user_withdrawn_books():
    if person is None:
        return index('GET')

    all_withdrawn = BooksWithdrawn.objects.all()
    res = []

    if all_withdrawn:
        for w in all_withdrawn:
            if w.withdrawerid == person.ucid:
                res.append(w.bookid)

    print(res)
    return res


def requestBooks(request):
    if person is None:
        return index('GET')

    if request.method == 'GET':
        form = RequestNewBookForm()
        return HttpResponseRedirect('/welcome/')
    else:
        form = RequestNewBookForm(request.POST)

        if form.is_valid():
            query_name = form.cleaned_data('bname')
            query_author = form.cleaned_data('bauthor')
            query_publisher = form.cleaned_data('bpublisher')
            query_year = form.cleaned_data('byear')
            query_lang = form.cleaned_data('blanguage')

        BooksRequest.objects.create(
            requestid=person.ucid, book_name=query_name, book_author=query_author, book_year=query_year, book_publisher=query_author, book_language=query_lang)

    return render(request, 'api/request.html', {'form': form})


'''
@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid:
            person = serializer.save()
            data['response'] = "success"
            data['ucid'] = person.ucid
            data['password'] = person.password
            else:
                data = serializer.errors
                return Response(data)
'''
