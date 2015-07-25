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
	DS_demandeur = models.CharField(max_length=20)
	DS_Sujet = models.CharField(max_length=30)
	DS_Desc = models.CharField(max_length=30)
	# Statut
	# priorite
	# Assigne a
	# Debut
	# Echeance
	# Temps estime
	# % realise
	# Fichiers
	# Observateurs

