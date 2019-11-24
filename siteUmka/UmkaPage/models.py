from django.db import models

#probleme de psycopg2 : installer via Outils -> Python -> Environnements Python -> vue d'ensemble -> ouvrir dans powerShell
#-> pip3 install psycopg2
#Remettre dans l'ordre les tables pour que les clés étrangères soient reconnues

class Personne(models.Model):
    idPersonne = models.AutoField(primary_key=True)

class Planning(models.Model):
    refPlanning = models.AutoField(primary_key=True)
    stockagePlanning = models.CharField(max_length=500)

class Administrateur(models.Model):
    idPersonne= models.IntegerField(primary_key=True)

    nomAdministrateur= models.CharField(max_length =50)
    prenomAdministrateur=models.CharField(max_length =50)
    mailAdministrateur=models.CharField(max_length =50)
    loginAdministrateur=models.CharField(max_length=50)
    motDePasseAdministrateur=models.CharField(max_length=50)

    refPlanning=models.ForeignKey(Planning, on_delete=models.CASCADE)


class TypeEvenement(models.Model):
    idTypeEvenement=models.AutoField(primary_key=True)

    libelleEvenement=models.CharField(max_length=50)

class Calendrier(models.Model):
    idEvenement=models.AutoField(primary_key=True)

    jourEvenement=models.DateField()
    moisEvenement=models.DateField()
    anneeEvenement=models.DateField()

    idTypeEvenement=models.ForeignKey(TypeEvenement, on_delete=models.CASCADE)

class Modifier(models.Model):
    idEvenement=models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    refEvenement=models.ForeignKey(Planning, on_delete=models.CASCADE)


class Article(models.Model):
    refArticle=models.AutoField(primary_key=True)

    nomArticle= models.CharField(max_length=50)
    contenuArticle= models.CharField(max_length=500)

class Editer(models.Model):
    refArticle=models.ForeignKey(Article, on_delete=models.CASCADE)
    idPersonne=models.ForeignKey(Administrateur, on_delete=models.CASCADE)



class Utilisateur(models.Model):
    idPersonne=models.IntegerField(primary_key=True)
    nomUtilisateur=models.CharField(max_length=50)
    prenomUtilisateur=models.CharField(max_length=50)
    mailUtilisateur=models.CharField(max_length=50)
    loginUtilisateur=models.CharField(max_length=50)
    motDePasseUtilisateur=models.CharField(max_length=50)

class TypeDocument(models.Model):
    typeDocument=models.AutoField(primary_key=True)

    libelleDocument=models.CharField(max_length=50)
    
class Document(models.Model):
    refDocument=models.AutoField(primary_key=True)

    nomDocument=models.CharField(max_length=50)
    tailleDocument=models.CharField(max_length=50)

    typeDocument=models.ForeignKey(TypeDocument, on_delete=models.CASCADE)

class Telecharger(models.Model):
    refDocument=models.ForeignKey(Document, on_delete=models.CASCADE)
    idPersonne=models.ForeignKey(Personne, on_delete=models.CASCADE)
    idUtilisateur=models.ForeignKey(Administrateur, on_delete=models.CASCADE)







