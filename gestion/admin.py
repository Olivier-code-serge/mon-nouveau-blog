from django.contrib import admin
from gestion.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','shirt_size', 'qte', 'prix', 'prix_total')
    list_filter = ('name', 'shirt_size')
    ordering = ('name',)
    search_fields = ('name',)
        
    fieldsets = [('Les différents articles ', {'fields':['name','shirt_size','prix','qte']})]
        
    def prix_total(self, prod):
        prix_total = prod.prix * prod.qte
        return prix_total, " F"

admin.site.register(Person, PersonAdmin)


