from django import forms


class LoginForm(forms.Form):
    ucid = forms.IntegerField(label="ucid", max_value=999999999)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    ucid = forms.IntegerField(label="ucid", max_value=999999999)
    name = forms.CharField(label="name", max_length=30)
    faculty = forms.CharField(label="faculty", max_length=30)
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)


class SearchBookForm(forms.Form):
    book_name = forms.CharField(label="book_name", max_length=50)
