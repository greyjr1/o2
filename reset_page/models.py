from django.db import models
from hole.models import Area
# Create your models here.


class Reset(models.Model):
    new_status = models.IntegerField()
    data = models.DateField()
    time = models.TimeField()
    comment = models.CharField(max_length=2048)

    def __str__(self):
        return self.comment


class Staff(models.Model):
    table_number = models.IntegerField()
    surname_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=100)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)


