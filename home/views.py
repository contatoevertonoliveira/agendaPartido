from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from home.models import Membro
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def home(request):
    if request.POST:
        nameM = request.POST.get('name')
        emailM = request.POST.get('email')
        endM = request.POST.get('end')
        cityM = request.POST.get('city')
        ufM = request.POST.get('uf')
        nameInstM = request.POST.get('namei')
        dateInstM = request.POST.get('datai')
        qtdeInstM = request.POST.get('qtdem')
        infoInstM = request.POST.get('info')
        
        member_id = request.POST.get('member_id')
        if member_id:
            member = Membro.objects.get(id=member_id)
            if member.nameM == nameM:
                member.emailM = emailM
                member.endM = endM
                member.cityM = cityM
                member.ufM = ufM
                member.nameInstM = nameInstM
                member.dateInstM = dateInstM
                member.membersQt = qtdeInstM
                member.infoInstM = infoInstM
                member.save()
            else:
                Membro.objects.create(
                    nameM = nameM,
                    emailM = emailM,
                    endM = endM,
                    cityM = cityM,
                    ufM = ufM,
                    nameInstM = nameInstM,
                    dateInstM = dateInstM,
                    membersQt = qtdeInstM,
                    infoInstM = infoInstM
                )
    return redirect ('/')

@login_required(login_url='/login/')
def listMembers(request):
    nameInstM = request.nameInstM
    member = Membro.objects.filter(nameM=nameInstM).values('id','nameM')
    dados = {'Instituto:':nameInstM}
    return JsonResponse(list(member), safe=False)