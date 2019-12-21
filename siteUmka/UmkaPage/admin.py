from django.contrib import admin
from .models import * #importation de toutes les tables pour les utiliser en mode admin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nomArticle', 'contenuArticle')
    list_display=('photoArticle','nomArticle')
    list_filter = ('nomArticle', 'contenuArticle')
    date_hierarchy = 'dateArticle'
    search_fields = ('nomArticle', 'contenuArticle')

    fieldsets = (
        ('Général', {
            #'classes': ['collapse', ],#classes CSS supplémentaires à appliquer sur le fieldset (wide, extrapretty et collapse)
            'fields':('nomArticle', )#fields est la liste des champs à afficher dans le fieldset
            #champs contenant les informations à éditer
            }),

            ('Ajouter une photo', {
                'description': 'Insérez la photo',
                'fields': ('photoArticle', )
                    }),

                ('Contenu de l\'article', {
                    'description': 'Le formulaire accepte les balises HTML.',
                    'fields': ('contenuArticle', )
                    }),
        )
   
    def apercu_contenu(self, article):
        text = article.contenuArticle[0:10]
        if len(article.contenu)>40:
            return '%s...' % text
        else:
            return text

    apercu_contenu.short_description = 'Apercu du contenu'

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Ajouter)




