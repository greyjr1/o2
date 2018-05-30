from django.conf.urls import url
from .views import index
from . import views
from django.views.generic import ListView, DetailView
from reset_page.models import Reset

urlpatterns = [
    url(r'^$', index),

    # url(r'^$', ListView.as_view(queryset=Reset.objects.all().order_by("-data")[:3], template_name="r_page/parts.html")),
]
