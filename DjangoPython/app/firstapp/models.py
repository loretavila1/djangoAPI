from django.db import models

# Create your models here.

class Cellphones(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    brand = models.CharField(max_length=250, blank=True, null=True)
    color = models.CharField(max_length=250, blank=True, null=True)
    company = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cellphones'


class Companies(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'
