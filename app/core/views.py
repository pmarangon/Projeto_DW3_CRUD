from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
  contexto = {'home': True,
              'agenda' :False}
  return render(request, 'home.html', contexto)
