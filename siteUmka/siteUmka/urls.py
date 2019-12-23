from django.conf.urls import url
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
#from django.contrib.auth.views import login #creer une view login et son url qu'on doit ecrire

urlpatterns =[
    url('admin/', admin.site.urls, name='admin'),
    path('', views.articles, name='articles'),



    path('informations', views.informations, name='infos'),
    path('apprentissage', views.apprentissage, name='enseignement'),
    path('celebrations', views.celebrations, name='fetes'),
    path('chansons',views.chantons, name='chansons'),
    path('collaborations', views.collaboration, name='collaborations'),
    path('dessiner', views.dessiner, name='dessin'),
    path('jouer', views.jouer, name='jeu'),
    path('organiser', views.organiser, name='organiser'),


    
    path('article/<int:id>', views.lire, name='lire'),
    #url(r'^$', views.home),

   #path('', include('posts.urls')),
    ]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA.ROOT)