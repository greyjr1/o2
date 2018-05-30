from django.shortcuts import render

# Create your views here.
from ie.models import Ie


def ie_temp(request):
    instr = Ie.objects.all()
    spisok = {'ieblin': instr}
    return render(request, "ie/manual.html", context=spisok)
