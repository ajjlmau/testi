from django.db import models

# Create your models here.

class Distro(models.Model):
    nimi = models.CharField(max_length=50)
    kuvaus = models.TextField(max_length=2500)
    kuva = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nimi