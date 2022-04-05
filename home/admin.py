from django.contrib import admin
from home.models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
  list_display = ('id','nameM','emailM','nameInstM')
  list_filter = ('nameM','nameInstM','cityM', 'ufM')
  search_fields = ('nameM','nameInstM','cityM','ufM')
  
# admin.site.register(Membro, MembroAdmin)