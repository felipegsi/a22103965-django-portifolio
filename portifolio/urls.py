from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [

    #
    path('testeNav', views.testeNav, name='testeNav'),

    path('', views.home_base, name='home'),
    # path('layout_base', views.layout_base, name='layout_base'),
    path('sobreMim_base', views.sobreMim_base, name='sobreMim_base'),
    path('sobreMim_base_2', views.sobreMim_base_2, name='sobreMim_base_2'),



    #
    path('sobreMimFull', views.sobreMimFull, name='sobreMimFull'),



    path('projetos', views.projetos_base, name='projetos'),
    path('contacto', views.contacto_base, name='contacto'),

    path('home_tarefa', views.home_tarefa, name='home_tarefa'),
    path('nova_tarefa', views.nova_tarefa, name='nova_tarefa'),
    path('edita_tarefa/<int:tarefa_id>/', views.edita_tarefa, name='edita_tarefa'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa, name='apaga_tarefa'),

    path('flights', views.flights_view, name='flights'),
    path('flight/<int:flight_id>', views.flight_view, name='flight'),
    path('add/<int:flight_id>', views.add_passenger_view, name='add'),
    path('remove/<int:flight_id>/<int:passenger_id>', views.remove_passenger_view, name='remove'),
    path('passengers', views.passengers_view, name='passengers'),
    path('passenger/<int:passenger_id>', views.passenger_view, name='passenger'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('home_blog', views.home_blog, name='home_blog'),

    path('home_sobreMim', views.home_sobreMim, name='home_sobreMim'),
    path('novo_sobreMim', views.novo_sobreMim, name='novo_sobreMim'),
    path('edita_sobreMim/<int:sobreMim_id>/', views.edita_sobreMim, name='edita_sobreMim'),
    path('apaga_sobreMim/<int:sobreMim_id>', views.apaga_sobreMim, name='apaga_sobreMim'),

    path('categorias_blog', views.categorias_blog, name='categorias_blog'),
    path('categoria_blog/<int:categoria_id>', views.categoria_blog, name='categoria_blog'),
    path('add_artigo_blog/<int:categoria_id>', views.add_artigo_blog, name='add_artigo_blog'),
    path('remove_artigo_blog/<int:categoria_id>/<int:artigo_id>', views.remove_artigo_blog, name='remove_artigo_blog'),
    path('artigos_blog', views.artigos_blog, name='artigos_blog'),
    path('artigo_blog/<int:artigo_id>', views.artigo_blog, name='artigo_blog'),
    path('login_blog', views.login_blog, name='login_blog'),
    path('logout_blog', views.logout_blog, name='logout_blog'),

]
