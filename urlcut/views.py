from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    return render(request, "urlcut/homepage.html")


def LoginPage(request):
    return render(request, "urlcut/login.html")


def SignupPage(request):
    return render(request, "urlcut/signup.html")