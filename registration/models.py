from django.db import models

# Create your models here.


class BirthRegistration(models.Model):
    dad_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    child_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)


class MarriageRegistration(models.Model):
    groom_name = models.CharField(max_length=255)
    bride_name = models.CharField(max_length=255)
    date_of_marriage = models.DateField()
    place_of_marriage = models.CharField(max_length=255)
    witnesses_names = models.CharField(max_length=255)


class DivorceRegistration(models.Model):
    husband_name = models.CharField(max_length=255)
    wife_name = models.CharField(max_length=255)
    date_of_divorce = models.DateField()
    place_of_divorce = models.CharField(max_length=255)


class DeathRegistration(models.Model):
    deceased_name = models.CharField(max_length=255)
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=255)
    cause_of_death = models.CharField(max_length=255)
