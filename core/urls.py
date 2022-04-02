from django.urls import path
from core.views import *

urlpatterns = [
  path('', lista_eventos),
  path('lista/', json_lista_eventos),
  path('evento/', evento),
  path('evento/submit', submit_evento),
  path('evento/delete/<int:id_evento>/', delete_evento),
  path('evento/historico/', lista_historico),
]