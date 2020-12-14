from django import forms


class LoginForm(forms.Form):
    ucid = forms.IntegerField(label="Enter your UCID ", max_value=999999999)
    password = forms.CharField(
        label="Enter your Password ", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    ucid = forms.IntegerField(label="Enter your UCID ", max_value=999999999)
    name = forms.CharField(label="Enter your Name ", max_length=30)

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

    faculty = forms.ChoiceField(
        label="Select from the following faculties ", choices=FACULTYCHOICES)
    password = forms.CharField(
        label="Enter your password ", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm your password ", widget=forms.PasswordInput)

    STUDENT = 'STUDENT'
    PROFESSOR = 'PROFESSOR'

    P_TYPE = ((STUDENT, 'Student'),
              (PROFESSOR, 'Professor'))

    ptype = forms.ChoiceField(label="Who are you? ", choices=P_TYPE)

    addi = forms.CharField(
        label="Enter your major (if student) or Years you've taught at UofC (if professor) ", max_length=25)


class SearchBookForm(forms.Form):
    book_name = forms.CharField(
        label="Search the book by it's name ", max_length=50, required=False)
    book_id = forms.IntegerField(
        label="Search the book by it's ID", max_value=999, required=False)
    series_name = forms.CharField(
        label="Search all books from series ", max_length=50, required=False)

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
        label="Search by the book type/Genre ", choices=BOOK_TYPES, required=False)

    author_name = forms.CharField(
        label="Search the books written by ", max_length=50, required=False)

    publisher_name = forms.CharField(
        label="Search the books published by ", max_length=50, required=False)


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField(
        label="Enter the id of the book you want to borrow ", max_value=999)


class ReturnBookForm(forms.Form):
    book_id = forms.IntegerField(
        label="ID of the you want to return ", max_value=999, required=True)


class RequestNewBookForm(forms.Form):
    bname = forms.CharField(label="Book Name", max_length=50)
    bauthor = forms.CharField(label="Author Name", max_length=50)
    bpublisher = forms.CharField(
        label="Publisher Name", max_length=50, required=False)
    byear = forms.IntegerField(label="Publishing Year", max_value=2021)
    blanguage = forms.CharField(
        label="Language", max_length=10, required=False)
    partS = forms.BooleanField(label="Is it a part of Series")
