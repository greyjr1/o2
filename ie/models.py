from django.db import models


# Create your models here.
class Ie(models.Model):
    name_ie = models.CharField(max_length=20)
    content_ie = models.CharField(max_length=65535)

    def iefile(self):
        return ('ie' + self.id + '.docx')
