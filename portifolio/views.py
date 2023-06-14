from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import TarefaForm
from .models import Tarefa
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
    return render(request, 'portfolio/blog.html')


def home_tarefa(request):
    topicos = ['HTML', 'Java', 'Kotlin', 'Python', 'Django', 'JavaScript', 'CSS']

    context = {
        'topicos': topicos,
        'tarefas': Tarefa.objects.all()
    }

    return render(request, 'portfolio/tarefas/home_page.html', context)


def nova_tarefa(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portifolio:nova_tarefa')

    context = {'form': form}

    return render(request, 'portfolio/tarefas/nova_tarefa.html', context)


def edita_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portifolio:edita_tarefa'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'portfolio/tarefas/edita_tarefa.html', context)


def apaga_tarefa(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portifolio:home_tarefa'))
