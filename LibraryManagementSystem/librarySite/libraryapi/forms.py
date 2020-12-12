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


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField(label="book_id", max_value=999)


class ReturnBookForm(forms.Form):
    book_id = forms.IntegerField(
        label="book_id", max_value=999, required=True)


class RequestNewBookForm(forms.Form):
    book_name = forms.CharField(label="bname", max_length=50)
    book_author = forms.CharField(label="bauthor", max_length=50)
    book_publisher = forms.CharField(
        label="bpublish", max_length=50, required=False)
    book_year = forms.IntegerField(label="byear", max_value=2021)
    book_lan = forms.CharField(label="language", max_length=10, required=False)
