from django.db import models

# Create your models here.

## -------------------------------------------------
## Meta Class contenant certaines donnees de bases
## -------------------------------------------------

DEF_TFAC='DEFAUT'

class HoroDatage(models.Model):

	h_datcre = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
	h_datmod = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	statut = models.BooleanField(verbose_name='Actif', default=True)

	class Meta:
		abstract = True

class DService(HoroDatage):
	## Canal / Channel / type de demande
	TYPE_DS = (
		( 'ASS', 'Assistance' ),
		( 'DEP', 'Depannage'),
		( 'AUD', 'Audit' ),
		( 'DEV', 'Developpement' ),
		( 'DIV', 'Autres' ),
	)
	DS_Type = models.CharField(max_length=5, choices=TYPE_DS, default='ASS', verbose_name='Type')
	## A voir expression de Demandeur
	DS_TiersDemandeur = models.CharField(max_length=20, blank=True, verbose_name='Demandeur')
	## A voir expression de facturation
	DS_TiersFacture = models.CharField(max_length=20, default=DEF_TFAC, blank=True, verbose_name='Tiers Facture')

	DS_Sujet = models.CharField(blank=True, max_length=50, verbose_name='Sujet')
	DS_Desc = models.TextField( blank=True, verbose_name='Description')

	STATUT_DS = (
		( 'NEW', 'Nouvelle' ),
		( 'CLOSED', 'Termine' ),
		( 'ENC', 'En cours' ),
		( 'ATT', 'Attente' ),
	)
	DS_Statut = models.CharField(max_length=6, choices=STATUT_DS, default='NEW', verbose_name='Statut')
	
	PRIORITE_DS = (
		('N', 'NORMAL'),
		('U', 'URGENT'),
		('B', 'BLOQUANT'),
	)

	DS_Priorite = models.CharField(max_length=3, choices=PRIORITE_DS, default='N', verbose_name='Priorite')
	DS_Assigne  = models.CharField(max_length=30, blank=True, verbose_name='Assigne')

	DS_Horo_Debut = models.CharField(max_length=30, blank=True, verbose_name='Debut')
	DS_Horo_Fin = models.CharField(max_length=30, blank=True, verbose_name='Fin')
	DS_Echance = models.CharField(max_length=30, blank=True, verbose_name='Avant le')
	DS_TempsEstime = models.CharField(max_length=30, blank=True, verbose_name='Temps Estime')
	DS_TempsRealise = models.CharField(max_length=30, blank=True, verbose_name='Temps Realise')
	DS_PC_Realise = models.CharField(max_length=30, blank=True, verbose_name='% Realisation')
	# Fichiers
	# Observateurs

class Action(HoroDatage):
	AC_Qui = models.CharField(max_length=30, blank=True, verbose_name='Qui')
	AC_Quand = models.CharField(max_length=30, blank=True, verbose_name='Quand')
	AC_Quoi = models.CharField(max_length=30, blank=True, verbose_name='Quoi')
	AC_Temps_Passe = models.CharField(max_length=30, blank=True, verbose_name='Temps passe')
	AC_Type = models.CharField(max_length=30, blank=True, verbose_name='Type')

#class Fichiers(HoroDatage):
#	Fi_DS = models.CharField(max_length=30)
#	Fi_Desc = models.CharField(max_length=30)
#	Fi_Path = models.CharField(max_length=30)
#
#class Observateurs(HoroDatage):
#	Ob_DS = models.CharField(max_length=30)
#	Ob_User = models.CharField(max_length=30)
#	Ob_Group = models.CharField(max_length=30)
