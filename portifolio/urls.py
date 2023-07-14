from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [

    # path('layout_base', views.layout_base, name='layout_base'),
    path('testeNav', views.testeNav, name='testeNav'),
    path('home_full_template', views.home_full_template, name='home_full_template'),

    path('', views.home_base, name='home'),

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
    path('login_flight', views.login_flight, name='login_flight'),
    path('logout_flight', views.logout_flight, name='logout_flight'),

    path('sobreMim_video', views.sobreMim_video, name='sobreMim_video'),
    path('sobreMim_educacao', views.sobreMim_educacao, name='sobreMim_educacao'),
    path('sobreMim_Full', views.sobreMim_full, name='sobreMim_Full'),
    path('novo_sobreMim', views.novo_sobreMim, name='novo_sobreMim'),
    path('edita_sobreMim/<int:sobreMim_id>/', views.edita_sobreMim, name='edita_sobreMim'),
    path('apaga_sobreMim/<int:sobreMim_id>', views.apaga_sobreMim, name='apaga_sobreMim'),

    path('categorias_blog/', views.categorias_blog, name='categorias_blog'),
    path('categoria_blog/<int:categoria_id>/', views.categoria_blog, name='categoria_blog'),
    path('artigos_blog/', views.artigos_blog, name='artigos_blog'),
    path('artigo_blog/<int:artigo_id>/', views.artigo_blog, name='artigo_blog'),
    path('add_artigo_blog/', views.add_artigo_blog, name='add_artigo_blog'),
    path('editar_artigo_blog/<int:artigo_id>/', views.editar_artigo_blog, name='editar_artigo_blog'),
    path('apagar_artigo_blog/<int:artigo_id>/', views.apagar_artigo_blog, name='apagar_artigo_blog'),
    path('apagar_categoria_blog/<int:categoria_id>/', views.apagar_categoria_blog, name='apagar_categoria_blog'),
    path('add_categoria_blog/', views.add_categoria_blog, name='add_categoria_blog'),
    path('editar_categoria_blog/<int:categoria_id>/', views.editar_categoria_blog, name='editar_categoria_blog'),
    path('home_blog_full/', views.home_blog_full, name='home_blog_full'),
    path('login_blog', views.login_blog, name='login_blog'),
    path('logout_blog', views.logout_blog, name='logout_blog'),

    path('criar_cadeira_educacao/', views.criar_cadeira_educacao, name='criar_cadeira_educacao'),
    path('editar_cadeira_educacao/<int:pk>/', views.editar_cadeira_educacao, name='editar_cadeira_educacao'),
    path('apagar_cadeira_educacao/<int:pk>/', views.apagar_cadeira_educacao, name='apagar_cadeira_educacao'),
    path('detalhes_cadeira_educacao/<int:pk>/', views.detalhes_cadeira_educacao, name='detalhes_cadeira_educacao'),
    path('home_educacao/', views.home_educacao, name='home_educacao'),
    path('login_educacao', views.login_educacao, name='login_educacao'),
    path('logout_educacao', views.logout_educacao, name='logout_educacao'),

]
