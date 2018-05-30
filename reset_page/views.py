# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from reset_page.models import Reset


def index(request):

    perekl = Reset.objects.all()
    return render(request, 'r_page/parts.html', context={'all_resets': perekl})
