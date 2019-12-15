from django.shortcuts import render, HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from UmkaPage.models import Article


def home(request):
    numbers =[1,2,3,4,5]
    nom= 'UMKA'

    args= {'asso': nom, 'numbers': numbers}
    return render(request, 'UmkaPage/accueil.html', args)

def articles(request):
    #Affiche tous les articles
    articles = Article.objects.all() #selectionne tous les articles
    return render(request, 'UmkaPage/articles.html', {'derniers_articles': articles})

def lire(request, id):
   #Affiche un article complet
       try:
            article = Article.objects.get(id=refArticle)
       except Article.DoesNotExist:
            raise Http404

       return render(request, 'UmkaPage/lire.html', {'article': article})

