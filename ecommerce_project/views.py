from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        "title": "Home Page"
    }
    return render(request, "home_page.html", context)


def about(request):
    context = {
        "title": "About"
    }
    return render(request, "home_page.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "title": "contact",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
    if request.method == "POST":
        print(request.POST.get("fullname"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print(str(request.user.is_authenticated))
    if form.is_valid():
        print(form.cleaned_data)
        user = authenticate(request=request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
        print(str(request.user.is_authenticated))
        if user is not None:
            print(str(request.user.is_authenticated))
            login(request, user)
            print(str(request.user.is_authenticated))
            redirect("/login")
        else:
            print("Error")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
