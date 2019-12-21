from django.db import models

#probleme de psycopg2 : installer via Outils -> Python -> Environnements Python -> vue d'ensemble -> ouvrir dans powerShell
#-> pip3 install psycopg2
#Remettre dans l'ordre les tables pour que les clés étrangères soient reconnues



class Personne(models.Model):
    idPersonne = models.AutoField(primary_key=True)

    def __str__(self):
        return self.idPersonne

class Planning(models.Model):
    refPlanning = models.AutoField(primary_key=True)
    stockagePlanning = models.CharField(max_length=500)

    def __str__(self):
        return self.refPlanning

class Administrateur(models.Model):
    idPersonne= models.IntegerField(primary_key=True)
    nomAdministrateur= models.CharField(max_length =50)
    prenomAdministrateur=models.CharField(max_length =50)
    mailAdministrateur=models.CharField(max_length =50)
    loginAdministrateur=models.CharField(max_length=50)
    motDePasseAdministrateur=models.CharField(max_length=50)
    refPlanning=models.ForeignKey(Planning, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomAdministrateur
    
class TypeEvenement(models.Model):
    idTypeEvenement=models.AutoField(primary_key=True)
    libelleEvenement=models.CharField(max_length=50)

    def __str__(self):
        return self.idTypeEvenement

class Calendrier(models.Model):
    idEvenement=models.AutoField(primary_key=True)

    jourEvenement=models.DateField()
    moisEvenement=models.DateField()
    anneeEvenement=models.DateField()
    idTypeEvenement=models.ForeignKey(TypeEvenement, on_delete=models.CASCADE)

    def __str__(self):
        return self.idEvenement

class Modifier(models.Model):
    idEvenement=models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    refEvenement=models.ForeignKey(Planning, on_delete=models.CASCADE)

    def __str__(self):
        return self.idEvenement

class Article(models.Model):
    refArticle=models.AutoField(primary_key=True)
    
    nomArticle= models.CharField(max_length=50)
    contenuArticle= models.TextField(max_length=500)
    dateArticle = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    photoArticle = models.ImageField(upload_to="photos_ecole", blank=True)

    def __str__(self):
        return self.nomArticle

class Editer(models.Model):
    refArticle=models.ForeignKey(Article, on_delete=models.CASCADE)
    idPersonne=models.ForeignKey(Administrateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.refArticle

class Photo(models.Model):
    refPhoto=models.AutoField(primary_key=True)
    nomPhoto=models.CharField(max_length=50)
    datePhoto = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    stockagePhoto=models.ImageField(upload_to="photos_ecole", blank=True)

    def __str__(self):
        return self.nomPhoto

class Ajouter(models.Model):
    refPhoto=models.ForeignKey(Photo, on_delete=models.CASCADE)
    idPersonne=models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    ajouterPhoto=models.ImageField(upload_to="photos_ecole", blank=True)

    def __str__(self):
        return self.refPhoto

class Utilisateur(models.Model):
    idPersonne=models.IntegerField(primary_key=True)
    nomUtilisateur=models.CharField(max_length=50)
    prenomUtilisateur=models.CharField(max_length=50)
    mailUtilisateur=models.CharField(max_length=50)
    loginUtilisateur=models.CharField(max_length=50)
    motDePasseUtilisateur=models.CharField(max_length=50)

    def __str__(self):
        return self.idPersonne

class TypeDocument(models.Model):
    typeDocument=models.AutoField(primary_key=True)

    libelleDocument=models.CharField(max_length=50)

    def __str__(self):
        return self.libelleDocument
    
class Document(models.Model):
    refDocument=models.AutoField(primary_key=True)
    nomDocument=models.CharField(max_length=50)
    tailleDocument=models.CharField(max_length=50)
    typeDocument=models.ForeignKey(TypeDocument, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomDocument

class Telecharger(models.Model):
    refDocument=models.ForeignKey(Document, on_delete=models.CASCADE)
    idPersonne=models.ForeignKey(Personne, on_delete=models.CASCADE)
    idUtilisateur=models.ForeignKey(Administrateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.idPersonne





