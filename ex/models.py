from django.db import models
from django.core.exceptions import ValidationError

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

## ---------------
## Classe Client 
## ---------------
class Client(HoroDatage):
	
	Cli_Nom = models.CharField(max_length=30, verbose_name='Nom Client') 											#denomination du client
	Cli_Logo = models.ImageField(max_length=100, upload_to='logos',  blank=True, verbose_name='Logo')				#Logo du client
	Cli_Schema = models.ImageField(max_length=100, upload_to='schemas', blank=True, verbose_name='Schema Infra')	#Image Infra 
	Cli_Cnx = models.TextField(default='<a renseigner>', blank=True, verbose_name='Methode de connexion')			#Connexion a distance 
	Cli_Tfic = models.TextField(default='<a renseigner>', blank=True, verbose_name='Transfert de fichier')			#transfert de fichier
	#Contrats (M2M) (non traite)
	Cli_Infos_Div = models.TextField(blank=True, verbose_name='Infos diverses')				 						#Informations diverses

	def clean(self):
		if self.Cli_Nom != self.Cli_Nom.replace(' ', ''):
			raise ValidationError("Le Nom ne doit pas contenir d'espace.")

	def __unicode__(self):
		return self.Cli_Nom

## --------------
## Site Client
## --------------
class Site(HoroDatage):
	Si_Client = models.ForeignKey('Client')
	Si_Nom = models.CharField(max_length=30, verbose_name='Nom du site')
	Si_Adr = models.TextField(blank=True, verbose_name='Adresse')
	Si_Comment = models.TextField(blank=True, verbose_name='Commentaire')

	def clean(self):
		if self.Si_Nom != self.Si_Nom.replace(' ', ''):
			raise ValidationError("Le Nom ne doit pas contenir d'espace.")

	def __unicode__(self):
		return "%s:%s" % (self.Si_Client, self.Si_Nom)
	

## --------------------------------
## Intervenant Client / Contact
## --------------------------------
class IntervClient(HoroDatage):
	IC_Site = models.ForeignKey('Site')
	IC_Nom = models.CharField(max_length=30, verbose_name='Nom')
	IC_Mail = models.EmailField(max_length=50, blank=True, verbose_name='E-mail')
	IC_Tel = models.CharField(max_length=30, blank=True, verbose_name='Mobile')
	IC_Poste = models.CharField(max_length=30, blank=True, verbose_name='Tel Fixe')
	IC_Fonction = models.CharField(max_length=30, blank=True, verbose_name='Fonction')

	def __unicode__(self):
		return "%s:%s" % (self.IC_Site, self.IC_Nom)


## ---------------------
## infra / Serveurs 
## ---------------------
class Infra(HoroDatage):
	OS_TYPES = (
		('UNIX', 'UNIX'),
		('WIN', 'WINDOWS'),
		('AUT', 'AUTRES')
	)
	MACH_TYPES = (
		( 'VM', 'Machine Virtuelle'),
		('PHY', 'Physique')
	)
	In_Client = models.ForeignKey('Client')
	In_Nom = models.CharField(max_length=30, verbose_name='Nom')
	In_Type = models.CharField(max_length=3, choices=MACH_TYPES, default='VM', verbose_name='Type')
	In_IP = models.GenericIPAddressField(default='127.0.0.1', verbose_name='Adr IP')
	In_OSTYPE = models.CharField(max_length=5, choices=OS_TYPES, default='UNIX', verbose_name='Famille OS')
	In_OSVersion = models.CharField(max_length=30, blank=True, verbose_name='OS Version')
	In_Desc = models.TextField(default=' ',blank=True, verbose_name='Description')

	def __unicode__(self):
		return "%s:%s" % (self.In_Client, self.In_Nom)

## -------------------------
## Solution X3 / ABEL IMMO
## -------------------------
class Solution(HoroDatage):
	SOL_TYPES = (
		( 'PROD', 'PRODUCTION'),
		( 'TEST', 'TEST DEV'),
		( 'CNSL', 'CONSOLE'),
		( 'PPRD', 'PRE PRODUCTION'),
		( 'REC', 'RECETTE'),
		( 'FORM', 'FORMATION'),
		( 'PRA', 'SYNCHRO PRA'),
	)
	Sol_Client = models.ForeignKey('Client')
	Sol_Nom = models.CharField(max_length=30, verbose_name='Solution')
	Sol_Port = models.CharField(max_length=10, verbose_name='Port')
	Sol_User = models.CharField(max_length=30, verbose_name='User prop')
	Sol_ADXDIR = models.CharField(max_length=100, verbose_name='Racine ADXDIR')
	Sol_Type = models.CharField(max_length=5, choices=SOL_TYPES, default='TEST', verbose_name='Type')
	Sol_Desc = models.TextField(blank=True, verbose_name='Description')

	def __unicode__(self):
		return "%s:%s" % (self.Sol_Client, self.Sol_Nom)

##
## Base de donnees
##
class Bdd(HoroDatage):
	BDD_TYPES = (
		('ORA', 'ORACLE'),
		('SS', 'SQL SERVER'),
	)
	BDD_STYPES = (
		('PROD', 'PRODUCTION'),
		('TEST', 'TEST & DEV'),
		('2ND', 'SECONDAIRE'),
	)
	Bdd_Client = models.ForeignKey('Client')
	Bdd_Sid = models.CharField(max_length=20, verbose_name='SID')
	Bdd_Server = models.ForeignKey('Infra')
	Bdd_Version = models.CharField(max_length=20, blank=True, verbose_name='Version')
	Bdd_OraHome = models.CharField(max_length=50, blank=True, verbose_name='OracleHome')
	Bdd_Type = models.CharField(max_length=5, choices=BDD_TYPES, default='ORA', verbose_name='Type')
	Bdd_SousType = models.CharField(max_length=5, choices=BDD_STYPES, default='PROD', verbose_name='SousType')
	Bdd_Desc = models.TextField(blank=True, verbose_name='Description')

	def __unicode__(self):
		return "%s:%s" % (self.Bdd_Client, self.Bdd_Sid)


## -----------------------
## Code acces / user mdp
## -----------------------
class Acces(HoroDatage):
	Acc_Client = models.ForeignKey('Client')
	Acc_SOLAPP = models.CharField(max_length=50, verbose_name='Nom')
	Acc_LOGIN_USR = models.CharField(max_length=50, verbose_name='Utilisateur')
	Acc_PASSWORD = models.CharField(max_length=30, verbose_name='Mot de passe')
	Acc_COMMENT = models.CharField(max_length=100, blank=True, verbose_name='Commentaire')

	def __unicode__(self):
		return "%s:%s" % (self.Acc_Client, self.Acc_SOLAPP)

## -----------
## Licences
## -----------
class Licence(HoroDatage):
	LIC_TYPES = (
		( 'X3', 'X3'),
		( 'HRM', 'HRM PAIE'),
		( 'IMMO', 'ABEL IMMO'),
		( 'DIV', 'AUTRES'),
	)
	Lic_Client = models.ForeignKey('Client')
	Lic_Nom = models.CharField(max_length=100, blank=True, verbose_name='Description')
	Lic_Type = models.CharField(max_length=5, choices=LIC_TYPES, default='X3', verbose_name='Type')
	Lic_Image = models.ImageField(max_length=100, upload_to='licences', blank=True, verbose_name='Image')	#Licence

	def __unicode__(self):
		return "%s:%s" % (self.Lic_Client, self.Lic_Nom)
