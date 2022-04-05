from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Membro
from .forms import MembroForm

def homeView(request):
    return render(request, 'home/home.html')

def homeSubmit(request):
    form = MembroForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect(homeView)
    else:
        messages.error(request, "Cadastro não realizado. Tente Novamente, mais tarde!")
        return redirect(homeView)
    
    return redirect(request, 'home.html', {'form': form, 'member':member})
    
    
@login_required(login_url='login/')
def listMembers(request):
    members = Membro.objects.all().values('id','nameM','nameInstM')
    return JsonResponse(list(members), safe=False)

@login_required(login_url='login/')
def updateMember(request, id):
    member = Membro.objects.get(id=id)
    form = MembroForm(request.POST or None, instance=member)
    
    if form.is_valid():
        form.save()
        return redirect('homeView')
    return redirect(request, 'home.html', {'form': form, 'member':member})

@login_required(login_url='login/')
def deleteMember(request):
    member = Membro.objects.get(id=id)
    
    if request.method == 'POST':
        member.delete()
        return redirect('homeView')