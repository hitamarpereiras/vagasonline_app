from django.shortcuts import render
from .forms import CandidatoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    """Pagina principal do app"""
    return  render(request, 'site_appvagasonline/index.html')

def cadastro(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("SALVO!")
            return HttpResponseRedirect(reverse('cadastro'))
        else:
            print("ERROS:", form.errors)
    else:
        form = CandidatoForm()

    return render(request, 'site_appvagasonline/cadastro.html', {'form': form})