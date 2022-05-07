from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    def str(self):
        return self.nom + " " + self.prenom

class Compte(models.Model):
    numero = models.IntegerField(primary_key=True)
    date = models.DateField()
    solde = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def str(self):
        return self.numero

class Operation(models.Model):
    numero = models.IntegerField(primary_key=True)
    date = models.DateField()
    montant = models.FloatField()
    type = models.CharField(max_length=50)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    def str(self):
        return self.numero