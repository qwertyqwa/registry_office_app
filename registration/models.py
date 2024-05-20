from django.db import models

# Create your models here.


class BirthRegistration(models.Model):
    child_name = models.CharField(max_length=255)
    child_citizenship = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    dad_name = models.CharField(max_length=255)
    dad_citizenship = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_citizenship = models.CharField(max_length=255)
    address_registry_office = models.CharField(max_length=255)


class MarriageRegistration(models.Model):
    groom_name = models.CharField(max_length=255)
    groom_citizenship = models.CharField(max_length=255)
    groom_date_of_birth = models.DateField()
    groom_place_of_birth = models.CharField(max_length=255)
    bride_name = models.CharField(max_length=255)
    bride_citizenship = models.CharField(max_length=255)
    bride_date_of_birth = models.DateField()
    bride_place_of_birth = models.CharField(max_length=255)
    groom_new_surname = models.CharField(max_length=255)
    bride_new_surname = models.CharField(max_length=255)


class DivorceRegistration(models.Model):
    husband_name = models.CharField(max_length=255)
    husband_citizenship = models.CharField(max_length=255)
    husband_date_of_birth = models.DateField()
    husband_place_of_birth = models.CharField(max_length=255)
    wife_name = models.CharField(max_length=255)
    wife_citizenship = models.CharField(max_length=255)
    wife_date_of_birth = models.DateField()
    wife_place_of_birth = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    date_of_divorce = models.DateField()
    husband_new_surname = models.CharField(max_length=255)
    wife_new_surname = models.CharField(max_length=255)


class DeathRegistration(models.Model):
    deceased_name = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=255)
    address_registry_office = models.CharField(max_length=255)
