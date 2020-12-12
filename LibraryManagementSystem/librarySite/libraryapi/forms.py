from django import forms


class LoginForm(forms.Form):
    ucid = forms.IntegerField(label="ucid", max_value=999999999)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    ucid = forms.IntegerField(label="ucid", max_value=999999999)
    name = forms.CharField(label="name", max_length=30)

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

    faculty = forms.ChoiceField(label="faculty", choices=FACULTYCHOICES)
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)


class SearchBookForm(forms.Form):
    book_name = forms.CharField(
        label="book_name", max_length=50, required=False)
    book_id = forms.IntegerField(
        label="book_id", max_value=999, required=False)
    series_name = forms.CharField(
        label="series_name", max_length=50, required=False)

    NONE = 'NONE'
    OTHER = 'OTHER'
    BIOGRAPHY = 'BIOGRAPHY'
    FICTION = 'FICTION'
    NONFICTION = 'NON-FICTION'

    BOOK_TYPES = ((NONE, 'None'),
                  (OTHER, 'Other'),
                  (BIOGRAPHY, 'Biography'),
                  (FICTION, 'Fiction'),
                  (NONFICTION, 'Non-Fiction'))

    book_type = forms.ChoiceField(
        label="Search by the book type/Genre: ", choices=BOOK_TYPES, required=False)

    author_name = forms.CharField(
        label="Search the books written by: ", max_length=50, required=False)

    publisher_name = forms.CharField(
        label="Search the books published  by: ", max_length=50, required=False)


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField(label="book_id", max_value=999)


class ReturnBookForm(forms.Form):
    book_id = forms.IntegerField(
        label="book_id", max_value=999, required=True)


class RequestNewBookForm(forms.Form):
    bname = forms.CharField(label="Book Name", max_length=50)
    bauthor = forms.CharField(label="Author", max_length=50)
    bpublisher = forms.CharField(
        label="Publisher", max_length=50, required=False)
    byear = forms.IntegerField(label="Year", max_value=2021)
    blanguage = forms.CharField(
        label="Language", max_length=10, required=False)
    partS = forms.BooleanField(label="Is it a part of Series")
