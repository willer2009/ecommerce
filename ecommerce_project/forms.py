from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "fullname",
                                                             "placeholder": "Name", "name": "fullname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "email",
                                                            "placeholder": "Your Email", "name": "email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "content",
                                                           "placeholder": "Your content", "name": "content"}))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)