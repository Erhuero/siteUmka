from django.shortcuts import render, HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from UmkaPage.models import *



def informations(request):
    articles = Article.objects.all()
    return render(request, 'UmkaPage/nosInfos.html')

def apprentissage(request):
    return render(request, 'UmkaPage/nousApprenons.html')

def celebrations(request):
    return render(request,'UmkaPage/nousCelebrons.html')

def chantons(request):
    return render(request, 'UmkaPage/nousChantonsDansons.html')

def collaboration(request):
    return render(request, 'UmkaPage/nousColaborons.html')

def dessiner(request):
    return render(request, 'UmkaPage/nousDessinons.html')

def jouer(request):
    return render(request, 'UmkaPage/nousJouons.html')

def organiser(request):
    return render(request, 'UmkaPage/nousOrganisons.html')


def articles(request):
    #Affiche tous les articles
    articles = Article.objects.all() #selectionne tous les articles
    photos = Photo.objects.all()
    return render(request, 'UmkaPage/articles.html', {'derniers_articles': articles})

def lire(request, id):
   #Affiche un article complet
       try:
            article = Article.objects.get(id=refArticle)
       except Article.DoesNotExist:
            raise Http404

       return render(request, 'UmkaPage/lire.html', {'article': article})

def insertion_photo(request):
    sauvegarde = False
    validation = nouvelleValidation(request.POST or None, rerequest.FILES)
    if validation.is_valid():
        photoArticle = Article()
        photoArticle = sauvegarde.cleaned_data["photo"]
        photoArticle.save()
        sauvegarde = True

    return render(request, 'articles.html', {
        'validation': validation,
        'sauvegarde': sauvegarde,
        })

def voir_photos(request):
    return render(
        request,
        'articles.html',
        {'photos': Photo.objects.all()}
    )
    

