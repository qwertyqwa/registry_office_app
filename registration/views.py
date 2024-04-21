from django.shortcuts import render, redirect, get_object_or_404
from registration.forms import *
# Create your views here.


def index(request):
    context = {
        'title': 'ЗАГС | Главная'
    }

    return render(request, 'registration/index.html', context=context)


def birth_registration(request):
    if request.method == 'POST':
        form = BirthRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = BirthRegistrationForm()

    birth_registrations = BirthRegistration.objects.all()

    context = {
        'title': 'ЗАГС | Регистрация рождения детей',
        'form': form,
        'birth_registrations': birth_registrations
    }

    return render(request, 'registration/birth_registration.html', context=context)


def marriage_registration(request):
    if request.method == 'POST':
        form = MarriageRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = MarriageRegistrationForm()

    marriage_registrations = MarriageRegistration.objects.all()

    context = {
        'title': 'ЗАГС | Регистрация бракосочетаний',
        'form': form,
        'marriage_registrations': marriage_registrations
    }

    return render(request, 'registration/marriage_registration.html', context=context)


def divorce_registration(request):
    if request.method == 'POST':
        form = DivorceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = DivorceRegistrationForm()

    divorce_registrations = DivorceRegistration.objects.all()

    context = {
        'title': 'ЗАГС | Регистрация бракосочетаний',
        'form': form,
        'divorce_registrations': divorce_registrations
    }

    return render(request, 'registration/divorce_registration.html', context=context)


def death_registration(request):
    if request.method == 'POST':
        form = DeathRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = DeathRegistrationForm()

    death_registrations = DeathRegistration.objects.all()

    context = {
        'title': 'ЗАГС | Регистрация бракосочетаний',
        'form': form,
        'death_registrations': death_registrations
    }

    return render(request, 'registration/death_registration.html', context=context)


def delete_records(request, model_name, record_id):
    model_map = {
        'birth': BirthRegistration,
        'marriage': MarriageRegistration,
        'divorce': DivorceRegistration,
        'death': DeathRegistration,
    }

    model = model_map.get(model_name)
    if not model:
        return render(request, 'index')

    instance = get_object_or_404(model, pk=record_id)
    instance.delete()

    return redirect('registration:{model_name}_registration'.format(model_name=model_name))
