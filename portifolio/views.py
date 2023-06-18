from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TarefaForm, PassengerForm, FlightForm
from .models import *
import datetime


# Create your views here.

def home(request):
    return render(request, 'portfolio/base/home.html')


def layout_base(request):
    return render(request, 'portfolio/base/layout_base.html')


def sobreMim(request):
    return render(request, 'portfolio/base/sobreMim.html')


def projetos(request):
    return render(request, 'portfolio/base/projetos.html')


def contacto(request):
    return render(request, 'portfolio/base/contacto.html')


def home_tarefa(request):
    topicos = ['HTML', 'Java', 'Kotlin', 'Python', 'Django', 'JavaScript', 'CSS']

    context = {
        'topicos': topicos,
        'tarefas': Tarefa.objects.all()
    }

    return render(request, 'portfolio/tarefas/home_tarefa.html', context)


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


def flights_view(request):
    print(request.user.username)

    context = {
        'flights': Flight.objects.all().order_by('origin')
    }
    return render(request, 'portfolio/flights/flights_view.html', context)


def flight_view(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'no_passengers': Passenger.objects.exclude(flights__in=[flight])
    }

    return render(request, 'portfolio/flights/flight_view.html', context)


def passengers_view(request):
    form = PassengerForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'passengers': Passenger.objects.all().order_by('name'),
        'form': PassengerForm(None),
    }
    return render(request, 'portfolio/flights/passengers_view.html', context)


def passenger_view(request, passenger_id):
    passenger = Passenger.objects.get(id=passenger_id)

    form = FlightForm(request.POST or None, instance=passenger)
    if form.is_valid():
        form.save()

    context = {
        'passenger': passenger,
        'form': form,
    }

    return render(request, 'portfolio/flights/passenger_view.html', context)


@login_required
def add_passenger_view(request, flight_id):
    flight = Flight.objects.get(id=flight_id)

    if request.method == 'POST':
        passenger = Passenger.objects.get(id=request.POST['passenger'])
        flight.passengers.add(passenger)

    return redirect('portifolio:flight', flight_id=flight_id)


@login_required
def remove_passenger_view(request, flight_id, passenger_id):
    flight = Flight.objects.get(id=flight_id)
    passenger = Passenger.objects.get(id=passenger_id)

    flight.passengers.remove(passenger)

    return redirect('portifolio:flights', flight_id=flight_id)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:flights')
        else:
            return render(request, 'portfolio/flights/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/flights/login.html')


def logout_view(request):
    logout(request)
    return redirect('portifolio:flights')


def home_blog(request):
    return render(request, 'portfolio/blog/home_blog.html')
