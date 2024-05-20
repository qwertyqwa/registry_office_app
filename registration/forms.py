from django import forms
from .models import BirthRegistration, MarriageRegistration, DivorceRegistration, DeathRegistration


class BirthRegistrationForm(forms.ModelForm):
    class Meta:
        model = BirthRegistration
        fields = [
            'child_name', 'child_citizenship', 'date_of_birth', 'place_of_birth',
            'dad_name', 'dad_citizenship', 'mother_name', 'mother_citizenship', 'address_registry_office'
        ]
        labels = {
            'child_name': 'ФИО ребенка',
            'child_citizenship': 'Гражданство',
            'date_of_birth': 'Дата рождения',
            'place_of_birth': 'Место рождения',
            'dad_name': 'ФИО отца',
            'dad_citizenship': 'Гражданство',
            'mother_name': 'ФИО матери',
            'mother_citizenship': 'Гражданство',
            'address_registry_office': 'Адрес ЗАГСа'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class MarriageRegistrationForm(forms.ModelForm):
    class Meta:
        model = MarriageRegistration
        fields = [
            'groom_name', 'groom_citizenship', 'groom_date_of_birth', 'groom_place_of_birth',
            'bride_name', 'bride_citizenship', 'bride_date_of_birth', 'bride_place_of_birth',
            'groom_new_surname', 'bride_new_surname'
        ]
        labels = {
            'groom_name': 'ФИО гражданина',
            'groom_citizenship': 'Гражданство',
            'groom_date_of_birth': 'Дата рождения',
            'groom_place_of_birth': 'Место рождения',
            'bride_name': 'ФИО невесты',
            'bride_citizenship': 'Гражданство',
            'bride_date_of_birth': 'Дата рождения',
            'bride_place_of_birth': 'Место рождения',
            'groom_new_surname': 'Новая фамилия жениха',
            'bride_new_surname': 'Новая фамилия невесты'
        }
        widgets = {
            'groom_date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bride_date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class DivorceRegistrationForm(forms.ModelForm):
    class Meta:
        model = DivorceRegistration
        fields = [
            'husband_name', 'husband_citizenship', 'husband_date_of_birth', 'husband_place_of_birth',
            'wife_name', 'wife_citizenship', 'wife_date_of_birth', 'wife_place_of_birth',
            'reason', 'date_of_divorce', 'husband_new_surname', 'wife_new_surname'
        ]
        labels = {
            'husband_name': 'ФИО мужа',
            'husband_citizenship': 'Гражданство',
            'husband_date_of_birth': 'Дата рождения',
            'husband_place_of_birth': 'Место рождения',
            'wife_name': 'ФИО жены',
            'wife_citizenship': 'Гражданство',
            'wife_date_of_birth': 'Дата рождения',
            'wife_place_of_birth': 'Место рождения',
            'reason': 'Причина развода',
            'date_of_divorce': 'Дата развода',
            'husband_new_surname': 'Новая фамилия мужа',
            'wife_new_surname': 'Новая фамилия жены'
        }
        widgets = {
            'husband_date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'wife_date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_divorce': forms.DateInput(attrs={'type': 'date'}),
        }


class DeathRegistrationForm(forms.ModelForm):
    class Meta:
        model = DeathRegistration
        fields = [
            'deceased_name', 'citizenship', 'place_of_birth', 'date_of_birth', 'date_of_death',
            'place_of_death', 'address_registry_office'
        ]
        labels = {
            'deceased_name': 'ФИО умершего',
            'citizenship': 'Гражданство',
            'place_of_birth': 'Место рождения',
            'date_of_birth': 'Дата рождения',
            'date_of_death': 'Дата смерти',
            'place_of_death': 'Место смерти',
            'address_registry_office': 'Адрес ЗАГСа'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
        }
