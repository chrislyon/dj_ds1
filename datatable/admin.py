from django.contrib import admin

# Register your models here.

from datatable.models import Serveur

# Register your models here.
class ServeurAdmin(admin.ModelAdmin):
	list_display = ('In_Type', 'In_Nom', 'In_IP', 'statut')
	list_filter = ('In_Type', 'In_Nom', 'In_IP', 'statut')
	search_fields = ['In_Type', 'In_Nom', 'In_IP' ]

admin.site.register(Serveur, ServeurAdmin)
