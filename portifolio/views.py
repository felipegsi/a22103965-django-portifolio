from django.shortcuts import render


# Create your views here.

def home(request):
    context = {
        'nome': 'FELIPE'
    }

    return render(request, 'portfolio/home.html')


def index(request):
    return render(request, 'portfolio/index.html')


def sobreMim(request):
    return render(request, 'portfolio/sobreMim.html')


def projetos(request):
    return render(request, 'portfolio/projetos.html')


def contacto(request):
    return render(request, 'portfolio/contacto.html')

def blog(request):
    return render(request, 'portfolio/blog.html')
