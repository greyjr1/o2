from django.db import models
# Create your models here.
from ie.models import Ie


class Area(models.Model):
    name_area = models.CharField(max_length=100)
    picture_area = models.BinaryField()
    description_area = models.CharField(max_length=2048)


class Equip(models.Model):
    type_equip = models.CharField(max_length=50)
    station_number = models.IntegerField()
    picture_equip = models.BinaryField()
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    ie_id = models.ForeignKey(Ie, on_delete=models.CASCADE)
