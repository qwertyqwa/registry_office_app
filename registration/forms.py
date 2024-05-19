from django import forms
from .models import BirthRegistration, MarriageRegistration, DivorceRegistration, DeathRegistration


class BirthRegistrationForm(forms.ModelForm):
    class Meta:
        GENDER_CHOICES = (
            ('Мужской', 'Мужской'),
            ('Женский', 'Женский')
        )

        model = BirthRegistration
        fields = ['dad_name', 'mother_name', 'child_name', 'date_of_birth', 'place_of_birth', 'gender']
        labels = {
            'dad_name': 'Имя отца',
            'mother_name': 'Имя матери',
            'child_name': 'Имя ребенка',
            'date_of_birth': 'Дата рождения',
            'place_of_birth': 'Место рождения',
            'gender': 'Пол'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=GENDER_CHOICES)
        }


class MarriageRegistrationForm(forms.ModelForm):
    class Meta:
        model = MarriageRegistration
        fields = ['groom_name', 'bride_name', 'date_of_marriage', 'place_of_marriage', 'witnesses_groom', 'witnesses_bride']
        labels = {
            'groom_name': 'Имя жениха',
            'bride_name': 'Имя невесты',
            'date_of_marriage': 'Дата бракосочетания',
            'place_of_marriage': 'Место бракосочетания',
            'witnesses_groom': 'Имена свидетелей жениха',
            'witnesses_bride': 'Имена свидетелей невесты'
        }

        widgets = {
            'date_of_marriage': forms.DateInput(attrs={'type': 'date'}),
        }


class DivorceRegistrationForm(forms.ModelForm):
    class Meta:
        model = DivorceRegistration
        fields = ['husband_name', 'wife_name', 'date_of_divorce', 'place_of_divorce']
        labels = {
            'husband_name': 'Имя мужа',
            'wife_name': 'Имя жены',
            'date_of_divorce': 'Дата развода',
            'place_of_divorce': 'Место развода'
        }

        widgets = {
            'date_of_divorce': forms.DateInput(attrs={'type': 'date'}),
        }


class DeathRegistrationForm(forms.ModelForm):
    class Meta:
        model = DeathRegistration
        fields = ['deceased_name', 'date_of_death', 'place_of_death', 'cause_of_death']
        labels = {
            'deceased_name': 'Имя умершего',
            'date_of_death': 'Дата смерти',
            'place_of_death': 'Место смерти',
            'cause_of_death': 'Причина смерти'
        }

        widgets = {
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
        }
