"""
Definition of urls for siteUmka.
"""

#from django.urls import path
from django.conf.urls import include, url
import UmkaPage.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()
urlpatterns = [

    #path('accueil', UmkaPage.views.home),
    # Examples:
    # url(r'^$', UmkaPage.views.accueil, name='accueil'), #le $ est le routage pour la racine du site
    #url(r'^siteUmka/', include('siteUmka.siteUmka.urls')),

    #url(r'^$home', UmkaPage.views.index, name='home'),

    

    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url('admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^UmkaPage', include('UmkaPage.urls')),
]
