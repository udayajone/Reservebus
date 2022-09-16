from django.db import models


class bus(models.Model):
    bus_name=models.CharField(max_length=20)
    bus_num=models.IntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=30)
    seats=models.IntegerField()
    balanseat=models.IntegerField()
    fare=models.IntegerField()
    date=models.DateField()
    time =models.TimeField()

