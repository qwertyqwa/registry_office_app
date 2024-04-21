from django.urls import path
from registration.views import *

app_name = 'registration'

urlpatterns = [
    path('birth_registration', birth_registration, name='birth_registration'),
    path('marriage_registration', marriage_registration, name='marriage_registration'),
    path('divorce_registration', divorce_registration, name='divorce_registration'),
    path('death_registration', death_registration, name='death_registration'),

    path('delete_record/<str:model_name>/<int:record_id>/', delete_records, name='delete_record'),
]
