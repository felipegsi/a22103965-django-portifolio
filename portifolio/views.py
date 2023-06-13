from django.shortcuts import render

import datetime


# Create your views here.

def home(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

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
    topicos = ['HTML', 'Java', 'Kotlin', 'Python', 'Django', 'JavaScript', 'CSS']

    context = {
        'topicos': topicos,
    }
    return render(request, 'portfolio/blog.html',context)
