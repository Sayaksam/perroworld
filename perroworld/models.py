from django.db import models

# Create your models here.


class Clinics(models.Model):
    name = models.CharField(max_length=2000)
    owner = models.CharField(max_length=500)
    address = models.CharField(max_length=2000)

    class Meta:
        db_table = "clinics"
