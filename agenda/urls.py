"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.views import *
from home.views import *
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('submit', home),
    # path('home/', RedirectView.as_view(url='/home/')),
    path('agenda/', lista_eventos),
    path('agenda/lista/', json_lista_eventos),
    path('agenda/evento/', evento),
    path('agenda/evento/submit', submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', delete_evento),
    path('agenda/evento/historico/', lista_historico),
    path('login/', login_user),
    path('login/submit', submit_login),
    path('logout/', logout_user),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
