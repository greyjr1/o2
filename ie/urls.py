from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ie_temp, name="ie_temp"),

]
