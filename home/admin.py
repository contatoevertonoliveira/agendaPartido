from django.contrib import admin
from home.models import Membro

class MembroAdmin(admin.ModelAdmin):
  list_display = ('id','nameM','emailM','endM','cityM','ufM','nameInstM','dateInstM','membersQt','infoInstM')
  list_filter = ('nameM','nameInstM',)
  
admin.site.register(Membro, MembroAdmin)