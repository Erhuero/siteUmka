from django.shortcuts import render, HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    numbers =[1,2,3,4,5]
    nom= 'UMKA'

    args= {'asso': nom, 'numbers': numbers}
    return render(request, 'UmkaPage/accueil.html', args)