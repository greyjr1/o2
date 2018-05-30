from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hole/homepage.html")


def tax(request):
    return render(request, "hole/tax_zone.html")


def one_more(request):
    return render(request, "hole/one_more.html")
