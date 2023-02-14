from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class BalJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class MumJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
