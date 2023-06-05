from django.shortcuts import render

# Create your views here.

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def index_page_view(request):
	return render(request, 'portfolio/home.html')

def sobreMim(request):
	return render(request, 'portfolio/sobreMim.html')

def projetos(request):
	return render(request, 'portfolio/projetos.html')

def contacto(request):
	return render(request, 'portfolio/contacto.html')