from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('', views.index_page_view, name='index'),
    path('sobreMim', views.sobreMim, name='sobreMim'),
    path('projetos', views.projetos, name='projetos'),
    path('contacto', views.contacto, name='contacto'),

]