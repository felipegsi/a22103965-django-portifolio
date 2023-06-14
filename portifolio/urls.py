from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('sobreMim', views.sobreMim, name='sobreMim'),
    path('projetos', views.projetos, name='projetos'),
    path('contacto', views.contacto, name='contacto'),
    path('blog', views.blog, name='blog'),
    path('home_tarefa', views.home_tarefa, name='home_tarefa'),
    path('nova_tarefa', views.nova_tarefa, name='nova_tarefa'),
    path('edita_tarefa/<int:tarefa_id>', views.edita_tarefa, name='edita_tarefa'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa, name='apaga_tarefa'),


]
