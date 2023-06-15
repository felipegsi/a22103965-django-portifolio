from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index_blog, name='index'),
    path('sobreMim', views.sobreMim, name='sobreMim'),
    path('projetos', views.projetos, name='projetos'),
    path('contacto', views.contacto, name='contacto'),
    path('home_tarefa', views.home_tarefa, name='home_tarefa'),
    path('nova_tarefa', views.nova_tarefa, name='nova_tarefa'),
    path('edita_tarefa/<int:tarefa_id>', views.edita_tarefa, name='edita_tarefa'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa, name='apaga_tarefa'),




    path('flights', views.flights_view, name='flights'),
    path('flight/<int:flight_id>', views.flight_view, name='flight'),
    path('add/<int:flight_id>', views.add_passenger_view, name='add'),
    path('remove/<int:flight_id>/<int:passenger_id>', views.remove_passenger_view, name='remove'),
    path('passengers', views.passengers_view, name='passengers'),
    path('passenger/<int:passenger_id>', views.passenger_view, name='passenger'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),


    path('layout_blog', views.layout_blog, name='layout_blog'),
    path('index_blog', views.index_blog, name='index_blog'),
    path('autores/', views.registrar_autor, name='registrar_autor'),
    path('artigos/novo/', views.criar_artigo, name='criar_artigo'),
    path('artigos/<int:id>/editar/', views.editar_artigo, name='editar_artigo'),
    path('artigos/<int:id>/apagar/', views.apagar_artigo, name='apagar_artigo'),

]
