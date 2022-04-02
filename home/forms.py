from django import forms
from .models import Membro

class MembroForm(forms.ModelForm):
  class Meta:
    model = Membro
    fields = ['nameM','emailM','endM','cityM','ufM','nameInstM','dateInstM','membersQt','infoInstM']