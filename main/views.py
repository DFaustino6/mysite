from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="inicio.html",)

def proporatividade(request):
	return render(request=request,
				  template_name="proporatividade.html",)

def minhasatividades(request):
	return render(request=request,
				  template_name="listaAtividades.html",)
