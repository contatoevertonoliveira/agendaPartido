from django.db import models
from datetime import datetime

class Membro(models.Model):
  # member_id = models.AutoField(primary_key=True)
  nameM = models.TextField(blank=True, null=True)
  emailM = models.TextField(blank=True, null=True)
  endM = models.TextField(blank=True, null=True)
  cityM = models.TextField(blank=True, null=True)
  ufM = models.TextField(blank=True, null=True)
  nameInstM = models.TextField(blank=True, null=True)
  dateInstM = models.TextField(blank=True, null=True)
  membersQt = models.IntegerField(blank=True, null=True)
  infoInstM = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = "members"