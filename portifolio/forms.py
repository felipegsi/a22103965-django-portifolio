from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from django import forms

from .models import *
class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

        # Para um conjunto de propriedade da classe (titulo, prioridade, concluido, etc),
        # o dicionário widgets permite configurar o elemento HTML input correspondente,
        # através de um dicionario de atributos de formatação (especificação de classes, placeholder, propriedades, etc).
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['name']


class FlightForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['flights']
        labels = {'flights': ''}
        help_texts = {'flights': 'Premir Ctrl para selecionar mais do que um'}




class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'