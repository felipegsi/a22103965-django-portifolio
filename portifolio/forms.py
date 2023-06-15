from django import forms
from django.forms import ModelForm
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


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'areas_interesse']

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['data', 'area', 'titulo', 'texto', 'imagem', 'link', 'comentarios']

    def __init__(self, *args, **kwargs):
        super(ArtigoForm, self).__init__(*args, **kwargs)
        self.fields['comentarios'].widget = forms.Textarea(attrs={'rows': 3})
