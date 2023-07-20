from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import *
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import requests
from bs4 import BeautifulSoup
import lxml


###############################################################
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
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/editar_cadeira_educacao.html',
                  {'form': form, 'cadeira': cadeira})


@login_required
def apagar_cadeira_educacao(request, pk):
    cadeira = get_object_or_404(Cadeira, pk=pk)
    if request.method == 'POST':
        cadeira.delete()
        return redirect('portifolio:home_educacao')
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/apagar_cadeira_educacao.html',
                  {'cadeira': cadeira})


def detalhes_cadeira_educacao(request, pk):
    cadeira = get_object_or_404(Cadeira, pk=pk)
    return render(request, 'portfolio/sobreMim/sobreMim_educacao_folder/detalhes_cadeira_educacao.html',
                  {'cadeira': cadeira})


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
            # aqui
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


def projetos_full(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos
    }
    return render(request, 'portfolio/projetos/projetos_full.html', context)


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
                  'portfolio/sobreMim/sobreMim_educacao_folder/templates/projetos/sobreMim/sobreMim_educacao.html',
                  context)


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

def home_full_template(request):
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque,
        'autores': autores
    }
    return render(request, 'portfolio/blog/blog_template_folder/home_full_template.html', context)


@login_required
def add_categoria_blog(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portifolio:home_full_template')
    else:
        form = CategoriaForm()
    context = {
        'form': form
    }
    return render(request, 'portfolio/blog/blog_template_folder/add_categoria_blog.html', context)


@login_required
def add_artigo_blog(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portifolio:home_full_template')
    else:
        form = ArtigoForm()
    context = {
        'form': form
    }
    return render(request, 'portfolio/blog/blog_template_folder/add_artigo_blog.html', context)


@login_required
def editar_categoria_blog(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('portifolio:home_full_template')
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form
    }
    return render(request, 'portfolio/blog/blog_template_folder/editar_categoria_blog.html', context)


@login_required
def editar_artigo_blog(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('portifolio:home_full_template')
    else:
        form = ArtigoForm(instance=artigo)
    context = {
        'form': form
    }
    return render(request, 'portfolio/blog/blog_template_folder/editar_artigo_blog.html', context)


@login_required
def apagar_categoria_blog(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('portifolio:home_full_template')
    context = {
        'categoria': categoria
    }
    return render(request, 'portfolio/blog/blog_template_folder/apagar_categoria_blog.html', context)


@login_required
def apagar_artigo_blog(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return redirect('portifolio:home_full_template')
    context = {
        'artigo': artigo
    }
    return render(request, 'portfolio/blog/blog_template_folder/apagar_artigo_blog.html', context)


def home_blog_full(request):
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque
    }
    return render(request, 'portfolio/blog/blog_template_folder/home_blog_full.html', context)


def categorias_blog(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'portfolio/blog/blog_template_folder/categorias_blog.html', context)


def categoria_blog(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    artigos = categoria.artigos.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()

    context = {
        'categoria': categoria,
        'artigos': artigos,
        'artigos_destaque': artigos_destaque,
        'autores': autores

    }
    return render(request, 'portfolio/blog/blog_template_folder/categoria_blog.html', context)


def artigos_blog(request):
    categorias = Categoria.objects.all()
    artigos = Artigo.objects.all()
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos': artigos,
        'autores': autores
    }
    return render(request, 'portfolio/blog/blog_template_folder/artigos_blog.html', context)


def artigo_blog(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque,
        'autores': autores,
        'artigo': artigo
    }
    return render(request, 'portfolio/blog/blog_template_folder/artigo_blog.html', context)


def login_blog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:home_full_template')
        else:
            # aqui
            return render(request, 'portfolio/blog/blog_template_folder/login_blog.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/blog/blog_template_folder/login_blog.html')


def logout_blog(request):
    logout(request)
    return redirect('portifolio:home_full_template')


####################################################
def web_home_full(request):
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque,
        'autores': autores
    }
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_home_full.html', context)


def web_laboratorios(request):
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque,
        'autores': autores
    }
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/web_laboratorios.html',
                  context)


def web_javaScript_playground(request):
    categorias = Categoria.objects.all()
    artigos_destaque = Artigo.objects.filter(destaque=True)
    autores = Autor.objects.all()
    context = {
        'categorias': categorias,
        'artigos_destaque': artigos_destaque,
        'autores': autores
    }
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_javaScript_playground.html', context)


def web_scrapping(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_scrapping.html')


def index_lab_1(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/index.html')


def info_lab_1(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/info.html')


def local_lab_1(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/local.html')


def multimidia_lab_1(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/multimedia.html')


def quizz_lab_1(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/quizz.html')


def html_css_lab_1(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/html5-css.html')


def index_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/indexNovo.html')


def sec2_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/sec2.html')


def sec3_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/sec3.html')


def sec4_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/sec4.html')


def sec5_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/sec5.html')


def sec6_lab_3(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab3/sec6.html')


def index_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/indexNovo2.html')


def animacoes_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/animacoes.html')


def imagensResponsivas_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/ImagensResponsivas.html')


def paralax_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/paralax.html')


def sec2_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/sec2.html')


def sec3_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/sec3.html')


def sec4_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/sec4.html')


def sec5_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/sec5.html')


def sec6_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/sec6.html')


def svg_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/svg.html')


def videoBackground_lab_4(request):
    return render(request,
                  'portfolio/sobreMim/sobreMim_programacao_web_folder/web_laboratorios_folder/lab1/lab4/videoBackground.html')


def web_calculator(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_calculator.html')


def web_tecnologias_existentes(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_tecnologias_existentes.html')


def web_video_tecnico(request):
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/web_video_tecnico.html')














def scraping_previsao_tempo(request):
    url = "https://www.amazon.com/Sony-Playstation-VR-Marvels-Bundle/dp/B0B2WDLQQP/ref=pd_vtp_h_pd_vtp_h_sccl_3/137-0687099-4683901?pd_rd_w=o5N1a&content-id=amzn1.sym.e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_p=e16c7d1a-0497-4008-b7be-636e59b1dfaf&pf_rd_r=YGYYMGMEE008NDP7NAR0&pd_rd_wg=8WZL2&pd_rd_r=93cc9a11-9c74-499a-8f26-9d4ed6268991&pd_rd_i=B0B2WDLQQP&psc=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en",
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")


    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    print(name)

    price = soup.select_one(selector="#price_inside_buybox").getText()

    print(price)


    context = {
        'name': name,
        'price': price
    }


    # Renderize o template HTML com os dados obtidos
    return render(request, 'portfolio/sobreMim/sobreMim_programacao_web_folder/scraping_previsao_tempo.html', context)




















def contacto_full(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            contato = Contato(nome=nome, email=email, telefone=telefone, assunto=assunto, mensagem=mensagem)
            contato.save()

            return render(request, 'portfolio/contacto/contacto_sucesso.html')
    else:
        form = ContatoForm()

    return render(request, 'portfolio/contacto/contacto_full.html', {'form': form})


def contacto_sucesso(request):
    return render(request, 'portfolio/contacto/contacto_sucesso.html')


def login_contacto(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:contacto_full')
        else:
            # aqui
            return render(request, 'portfolio/contacto/contacto_login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/contacto/contacto_login.html')


def logout_contacto(request):
    logout(request)
    return redirect('portifolio:contacto_full')


def contacto_todos_formularios(request):
    formularios = Contato.objects.all()
    context = {
        'formularios': formularios
    }
    return render(request, 'portfolio/contacto/contacto_todos_formularios.html', context)


@login_required
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save()
            return redirect('portifolio:detalhes_projeto', pk=projeto.pk)
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projetos/criar_projeto.html', {'form': form})


@login_required
def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portifolio:detalhes_projeto', pk=projeto.pk)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projetos/editar_projeto.html',
                  {'form': form, 'projeto': projeto})


@login_required
def apagar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portifolio:projetos_full')
    return render(request, 'portfolio/projetos/apagar_projeto.html',
                  {'projeto': projeto})


def detalhes_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projetos/detalhes_projeto.html',
                  {'projeto': projeto})


def login_projeto(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:projetos_full')
        else:
            # aqui
            return render(request, 'portfolio/projetos/login_projeto.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/projetos/login_projeto.html')


def logout_projeto(request):
    logout(request)
    return redirect('portifolio:projetos_full')
