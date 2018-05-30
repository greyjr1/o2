from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tax/', views.tax, name="tax"),
    url(r'^one_more/', views.one_more, name="one_more"),

]
