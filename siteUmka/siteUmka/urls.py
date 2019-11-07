"""
Definition of urls for siteUmka.
"""

from django.conf.urls import include, url
import UmkaPage.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', UmkaPage.views.index, name='index'), #le $ est le routage pour la racine du site
    #url(r'^siteUmka/', include('siteUmka.siteUmka.urls')),

    url(r'^$home', UmkaPage.views.index, name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
