from django.db import models

# Create your models here.

## -------------------------------------------------
## Meta Class contenant certaines donnees de bases
## -------------------------------------------------

class HoroDatage(models.Model):

	h_datcre = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
	h_datmod = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	statut = models.BooleanField(verbose_name='Actif', default=True)

	class Meta:
		abstract = True

class DService(HoroDatage):
	## Canal / Channel / type de demande
	DS_Type = models.CharField(max_length=20)
	## A voir expression de Demandeur
	DS_Demandeur = models.CharField(max_length=20)
	## A voir expression de facturation
	DS_Facture = models.CharField(max_length=20)

	DS_Sujet = models.CharField(max_length=30)
	DS_Desc = models.CharField(max_length=30)

	DS_Statut = models.CharField(max_length=30)
	DS_Priorite = models.CharField(max_length=30)
	DS_Assigne  = models.CharField(max_length=30)

	DS_Horo_Debut = models.CharField(max_length=30)
	DS_Horo_Fin = models.CharField(max_length=30)
	DS_Echance = models.CharField(max_length=30)
	DS_TempsEstime = models.CharField(max_length=30)
	DS_TempsRealise = models.CharField(max_length=30)
	DS_PC_Realise = models.CharField(max_length=30)
	# Fichiers
	# Observateurs

class Actions(HoroDatage):
	AC_Qui = models.CharField(max_length=30)
	AC_Quand = models.CharField(max_length=30)
	AC_Quoi = models.CharField(max_length=30)
	AC_Temps_Passe = models.CharField(max_length=30)
	AC_Type = models.CharField(max_length=30)

class Fichiers(HoroDatage):
	Fi_DS = models.CharField(max_length=30)
	Fi_Desc = models.CharField(max_length=30)
	Fi_Path = models.CharField(max_length=30)

class Observateurs(HoroDatage):
	Ob_DS = models.CharField(max_length=30)
	Ob_User = models.CharField(max_length=30)
	Ob_Group = models.CharField(max_length=30)
