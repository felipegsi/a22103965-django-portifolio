from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import *

@login_required
def criar_cadeira_educacao(request):
    if request.method == 'POST':
        form = CadeiraForm(request.POST, request.FILES)
        if form.is_valid():
            cadeira = form.save()
            return redirect('portifolio:detalhes_cadeira_educacao', pk=cadeira.pk)
    else:
        form = CadeiraForm()
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/criar_cadeira_educacao.html', {'form': form})

@login_required
def editar_cadeira_educacao(request, pk):
    cadeira = get_object_or_404(Cadeira, pk=pk)
    if request.method == 'POST':
        form = CadeiraForm(request.POST, instance=cadeira)
        if form.is_valid():
            form.save()
            return redirect('portifolio:detalhes_cadeira_educacao', pk=cadeira.pk)
    else:
        form = CadeiraForm(instance=cadeira)
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/editar_cadeira_educacao.html', {'form': form, 'cadeira': cadeira})

@login_required
def apagar_cadeira_educacao(request, pk):
    cadeira = get_object_or_404(Cadeira, pk=pk)
    if request.method == 'POST':
        cadeira.delete()
        return redirect('portifolio:home_educacao')
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/apagar_cadeira_educacao.html', {'cadeira': cadeira})


def detalhes_cadeira_educacao(request, pk):
    cadeira = get_object_or_404(Cadeira, pk=pk)
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/detalhes_cadeira_educacao.html', {'cadeira': cadeira})


def home_educacao(request):
    cadeiras = Cadeira.objects.all()
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/home_educacao.html', {'cadeiras': cadeiras})


def login_educacao(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:home_educacao')
        else:
            #aqui
            return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/login_educacao.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/login_educacao.html')


def logout_educacao(request):
    logout(request)
    return redirect('portifolio:home_educacao')











#######################################
def testeNav(request):
    return render(request, 'portfolio/base/testeNav.html')


def home_base(request):
    return render(request, 'portfolio/base/home_base.html')


def projetos_base(request):
    return render(request, 'portfolio/base/projetos_base.html')


def contacto_base(request):
    return render(request, 'portfolio/base/contacto_base.html')


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
        return HttpResponseRedirect(reverse('portifolio:edita_tarefa', args=[tarefa_id]))

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


def login_flight(request):
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
            return render(request, 'portfolio/flights/login_flight.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/flights/login_flight.html')


def logout_flight(request):
    logout(request)
    return redirect('portifolio:flights')


def home_blog(request):
    return render(request, 'portfolio/blog/base_blog.html')


###############################-----sobre_Mim_2------#####################################

def sobreMim_full(request):
    return render(request, 'portfolio/sobreMim/sobreMim_full.html')


def sobreMim_video(request):
    return render(request, 'portfolio/sobreMim/sobreMim_licencituras_folder/sobreMim_video.html')


def sobreMim_educacao(request):
    topicos = ['HTML', 'Java', 'Kotlin', 'Python', 'Django', 'JavaScript', 'CSS']

    context = {
        'topicos': topicos,
        'sobreMims': SobreMim.objects.all()
    }

    return render(request,
                  'portfolio/sobreMim/sobreMim_educacao_folder/templates/portfolio/sobreMim/sobreMim_educacao.html', context)


def novo_sobreMim(request):
    form = SobreMimForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portifolio:novo_sobreMim')

    context = {'form': form}

    return render(request, 'portfolio/sobreMim/sobreMim_licencituras_folder/sobreMim_nova_2.html', context)


def edita_sobreMim(request, sobreMim_id):
    sobreMim = SobreMim.objects.get(id=sobreMim_id)
    form = SobreMimForm(request.POST or None, instance=sobreMim)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portifolio:edita_sobreMim', args=[sobreMim_id]))

    context = {'form': form, 'sobreMim_id': sobreMim_id}
    return render(request, 'portfolio/sobreMim/sobreMim_licencituras_folder/sobreMim_edita_2.html', context)


def apaga_sobreMim(request, sobreMim_id):
    SobreMim.objects.get(id=sobreMim_id).delete()
    return HttpResponseRedirect(reverse('portifolio:sobreMim_educacao'))


########################################################################
def categorias_blog(request):
    print(request.user.username)
    categorias = Categoria.objects.all().order_by('nome')
    context = {
        'categorias': categorias
    }
    return render(request, 'portfolio/blog/categorias_blog.html', context)


def categoria_blog(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    artigos = Artigo.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'artigos': artigos,
    }
    return render(request, 'portfolio/blog/categoria_blog.html', context)


def artigos_blog(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'artigos': Artigo.objects.all().order_by('titulo'),
        'form': ArtigoForm(None),
    }
    return render(request, 'portfolio/blog/artigos_blog.html', context)


def artigo_blog(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    form = CategoriaForm(request.POST or None, instance=artigo)
    if form.is_valid():
        form.save()
    context = {
        'artigo': artigo,
        'form': form,
    }
    return render(request, 'portfolio/blog/artigo_blog.html', context)


@login_required
def add_artigo_blog(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)

    if request.method == 'POST':
        artigo = Artigo.objects.get(id=request.POST['artigo'])
        categoria.artigos_categoria.add(artigo)

    return redirect('portifolio:categoria_blog', categoria_id=categoria_id)


@login_required
def remove_artigo_blog(request, categoria_id, artigo_id):
    categoria = Categoria.objects.get(id=categoria_id)
    artigo = Artigo.objects.get(id=artigo_id)

    categoria.artigos_categoria.remove(artigo)

    return redirect('portifolio:categorias_blog', categoria_id=categoria_id)


def login_blog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:categorias_blog')
        else:
            return render(request, 'portfolio/blog/login_blog.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/blog/login_blog.html')


def logout_blog(request):
    logout(request)
    return redirect('portifolio:categorias_blog')
