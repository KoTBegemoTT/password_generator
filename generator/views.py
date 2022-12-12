from django.shortcuts import render
from django.shortcuts import HttpResponse
from random import choices


def home(request):
    return render(request, r"generator\home.html")


def password(request):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_symbols = '@#$%^&*(){}[]?!'

    password_symbols = letters
    length = int(request.GET.get("length"))
    uppercase, have_numbers, special = request.GET.get("uppercase"), request.GET.get("numbers"), request.GET.get("special")

    if uppercase:
        password_symbols += upper_letters
    if have_numbers:
        password_symbols += numbers
    if special:
        password_symbols += special_symbols

    generated_password = "".join(choices(password_symbols, k=length))
    return render(request, r"generator\password.html", {'password': generated_password})


def about(request):
    return render(request, r"generator\about.html")
