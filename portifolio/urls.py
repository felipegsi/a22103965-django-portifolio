from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [

    path('', views.home_base, name='home'),


    # Tarefas
    path('home_tarefa', views.home_tarefa, name='home_tarefa'),
    path('nova_tarefa', views.nova_tarefa, name='nova_tarefa'),
    path('edita_tarefa/<int:tarefa_id>/', views.edita_tarefa, name='edita_tarefa'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa, name='apaga_tarefa'),

    # Voos
    path('flights', views.flights_view, name='flights'),
    path('flight/<int:flight_id>', views.flight_view, name='flight'),
    path('add/<int:flight_id>', views.add_passenger_view, name='add'),
    path('remove/<int:flight_id>/<int:passenger_id>', views.remove_passenger_view, name='remove'),
    path('passengers', views.passengers_view, name='passengers'),
    path('passenger/<int:passenger_id>', views.passenger_view, name='passenger'),
    path('login_flight', views.login_flight, name='login_flight'),
    path('logout_flight', views.logout_flight, name='logout_flight'),

    # Sobre mim
    path('sobreMim_video', views.sobreMim_video, name='sobreMim_video'),
    path('sobreMim_Full', views.sobreMim_full, name='sobreMim_Full'),
    path('novo_sobreMim', views.novo_sobreMim, name='novo_sobreMim'),
    path('edita_sobreMim/<int:sobreMim_id>/', views.edita_sobreMim, name='edita_sobreMim'),
    path('apaga_sobreMim/<int:sobreMim_id>', views.apaga_sobreMim, name='apaga_sobreMim'),

    # Blog
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
    path('home_blog_full', views.home_blog_full, name='home_blog_full'),
    path('login_blog', views.login_blog, name='login_blog'),
    path('logout_blog', views.logout_blog, name='logout_blog'),

    # Cadeiras
    path('criar_cadeira_educacao/', views.criar_cadeira_educacao, name='criar_cadeira_educacao'),
    path('editar_cadeira_educacao/<int:pk>/', views.editar_cadeira_educacao, name='editar_cadeira_educacao'),
    path('apagar_cadeira_educacao/<int:pk>/', views.apagar_cadeira_educacao, name='apagar_cadeira_educacao'),
    path('detalhes_cadeira_educacao/<int:pk>/', views.detalhes_cadeira_educacao, name='detalhes_cadeira_educacao'),
    path('home_educacao/', views.home_educacao, name='home_educacao'),
    path('login_educacao', views.login_educacao, name='login_educacao'),
    path('logout_educacao', views.logout_educacao, name='logout_educacao'),

    # Programação Web
    path('web_home_full/', views.web_home_full, name='web_home_full'),
    path('web_laboratorios/', views.web_laboratorios, name='web_laboratorios'),
    path('web_javaScript_playground/', views.web_javaScript_playground, name='web_javaScript_playground'),
    path('web_scrapping/', views.web_scrapping, name='web_scrapping'),
    path('scraping_previsao_tempo/', views.scraping_previsao_tempo, name='scraping_previsao_tempo'),

    # Laboratório 1
    path('index_lab_1', views.index_lab_1, name='index_lab_1'),
    path('info_lab_1', views.info_lab_1, name='info_lab_1'),
    path('local_lab_1', views.local_lab_1, name='local_lab_1'),
    path('multimidia_lab_1', views.multimidia_lab_1, name='multimidia_lab_1'),
    path('quizz_lab_1', views.quizz_lab_1, name='quizz_lab_1'),
    path('html_css_lab_1', views.html_css_lab_1, name='html_css_lab_1'),

    # Laboratório 3
    path('index_lab_3', views.index_lab_3, name='index_lab_3'),
    path('sec2_lab_3', views.sec2_lab_3, name='sec2_lab_3'),
    path('sec3_lab_3', views.sec3_lab_3, name='sec3_lab_3'),
    path('sec4_lab_3', views.sec4_lab_3, name='sec4_lab_3'),
    path('sec5_lab_3', views.sec5_lab_3, name='sec5_lab_3'),
    path('sec6_lab_3', views.sec6_lab_3, name='sec6_lab_3'),

    # Laboratório 4
    path('index_lab_4', views.index_lab_4, name='index_lab_4'),
    path('animacoes_lab_4', views.animacoes_lab_4, name='animacoes_lab_4'),
    path('imagensResponsivas_lab_4', views.imagensResponsivas_lab_4, name='imagensResponsivas_lab_4'),
    path('paralax_lab_4', views.paralax_lab_4, name='paralax_lab_4'),
    path('paralax_lab_4', views.paralax_lab_4, name='paralax_lab_4'),
    path('sec2_lab_4', views.sec2_lab_4, name='sec2_lab_4'),
    path('sec3_lab_4', views.sec3_lab_4, name='sec3_lab_4'),
    path('sec4_lab_4', views.sec4_lab_4, name='sec4_lab_4'),
    path('sec5_lab_4', views.sec5_lab_4, name='sec5_lab_4'),
    path('sec6_lab_4', views.sec6_lab_4, name='sec6_lab_4'),
    path('svg_lab_4', views.svg_lab_4, name='svg_lab_4'),
    path('videoBackground_lab_4', views.videoBackground_lab_4, name='videoBackground_lab_4'),
    path('web_calculator', views.web_calculator, name='web_calculator'),
    path('web_tecnologias_existentes', views.web_tecnologias_existentes, name='web_tecnologias_existentes'),
    path('web_video_tecnico', views.web_video_tecnico, name='web_video_tecnico'),

    # Formulário de contacto
    path('contacto_full', views.contacto_full, name='contacto_full'),
    path('contacto_sucesso', views.contacto_sucesso, name='contacto_sucesso'),
    path('login_contacto', views.login_contacto, name='login_contacto'),
    path('logout_contacto', views.logout_contacto, name='logout_contacto'),
    path('contacto_todos_formularios', views.contacto_todos_formularios, name='contacto_todos_formularios'),

    # Projetos
    path('projetos_full', views.projetos_full, name='projetos_full'),
    path('criar_projeto/', views.criar_projeto, name='criar_projeto'),
    path('editar_projeto/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('apagar_projeto/<int:pk>/', views.apagar_projeto, name='apagar_projeto'),
    path('detalhes_projeto/<int:pk>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('login_projeto', views.login_projeto, name='login_projeto'),
    path('logout_projeto', views.logout_projeto, name='logout_projeto'),
    path('listaDeVisitantes_igreja', views.listaDeVisitantes_igreja, name='listaDeVisitantes_igreja'),
    path('registrarVisitante_igreja', views.registrarVisitante_igreja, name='registrarVisitante_igreja'),


    # Skills
    path('skills', views.skills, name='skills'),

    # Tests
    path('testeNav', views.testeNav, name='testeNav'),
    path('defesa', views.defesa, name='defesa'),

]
