from django.contrib import admin

from ds.models import DService
from ds.models import Action

# Register your models here.
class DServiceAdmin(admin.ModelAdmin):
	list_display = ('DS_Type', 'DS_TiersDemandeur', 'DS_Sujet', 'statut')
	list_filter = ('DS_Type', 'DS_TiersDemandeur', 'DS_Sujet', 'statut')
	search_fields = ['DS_Type', 'DS_TiersDemandeur', 'DS_Sujet' ]

class ActionAdmin(admin.ModelAdmin):
	list_display = ('AC_Type', 'AC_Qui', 'AC_Quoi', 'statut')
	list_filter = ('AC_Type', 'AC_Qui', 'AC_Quoi', 'statut')
	search_fields = ['AC_Type', 'AC_Qui', 'AC_Quoi' ]

admin.site.register(DService, DServiceAdmin)
admin.site.register(Action, ActionAdmin)
