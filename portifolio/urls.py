from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home_blog, name='index'),
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

    path('home_blog/', views.home_blog, name='home_blog'),
    path('criar_artigo/', views.criar_artigo, name='criar_artigo'),
    path('editar_artigo/<int:id>/', views.editar_artigo, name='editar_artigo'),
    path('apagar_artigo/<int:id>/', views.apagar_artigo, name='apagar_artigo'),
    path('registrar_autor/', views.registrar_autor, name='registrar_autor'),
    path('registrar_conta/', views.registrar_conta, name='registrar_conta'),
    path('area_restrita/', views.area_restrita, name='area_restrita'),
]
