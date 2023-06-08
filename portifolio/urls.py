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
]
