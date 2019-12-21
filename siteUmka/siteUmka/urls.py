from django.conf.urls import url
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
#from django.contrib.auth.views import login #creer une view login et son url qu'on doit ecrire

urlpatterns =[
    url('admin/', admin.site.urls),
    path('', views.articles, name='Articles'),
    path('article/<int:id>', views.lire, name='lire'),
    url(r'^$', views.home),

   #path('', include('posts.urls')),
    ]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA.ROOT)