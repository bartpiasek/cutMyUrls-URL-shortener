from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ShortUrl
import pyperclip
import os
import random, string

# Create your views here.
def homepage(request):
    return render(request, "urlcut/homepage.html")

# @login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    urls = ShortUrl.objects.filter(user = user)

    context = {
        'urls': urls
    }

    return render(request, "urlcut/dashboard.html", context)


def generate_random():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


def generate(request):
    # generate base on input
    if request.method == 'POST':
        if request.POST['original'] and request.POST['short']:
            user = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = ShortUrl.objects.filter(short_query = short)
            if not check:
                new_url = ShortUrl(
                    user = user,
                    original_url = original,
                    short_query = short,
                )
                new_url.save()
                return redirect(dashboard)
            else:
                messages.error(request, "Already exists")
                return redirect(dashboard)

        elif request.POST['original']:
            # genreate randomly - remove user, x - AnonymousUSer error 
            user = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = generate_random()
                check = ShortUrl.objects.filter(short_query = short)
                if not check:
                    new_url = ShortUrl(
                        user = user,
                        original_url = original,
                        short_query = short,
                    )
                    new_url.save()
                    # tutaj moze kopiowanie
                    return redirect(dashboard)
                else:
                    continue
        else:
            messages.error(request, "Empty fields")
            return redirect(dashboard)
    else:
        return redirect(dashboard)


# clipboard = pyperclip(['short'])
# def copy_url(request):
#     # tu musi byc cały url - lub moze czesc hardcoded + short w jakiejs zmiennej 
#     pyperclip.copy()
#     return render(request)
# dokladnie to samo co odpowiada za to co jest po short:

# def copy_shorturl():
#     pypercopy = short_query
#     return pyperclip.copy("http://localhost:8000/"+pypercopy)