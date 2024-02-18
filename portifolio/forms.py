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


class SobreMimForm(ModelForm):
    class Meta:
        model = SobreMim
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


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'  # or specify the desired fields explicitly


class CadeiraForm(forms.ModelForm):
    class Meta:
       model = Cadeira
       fields = '__all__'


class ContatoForm(forms.Form):
    ASSUNTO_CHOICES = [
        ('', 'Selecione o assunto'),
        ('duvida', 'Dúvida'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
        ('outro', 'Outro'),
    ]

    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}))
    telefone = forms.CharField(label='Telefone', max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite seu telefone'}))
    assunto = forms.ChoiceField(label='Assunto', choices=ASSUNTO_CHOICES)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder': 'Digite sua mensagem', 'rows': 5}))

    def clean_assunto(self):
        assunto = self.cleaned_data['assunto']
        if not assunto:
            raise forms.ValidationError('Selecione um assunto válido.')
        return assunto

class ProjetoForm(forms.ModelForm):
    class Meta:
       model = Projeto
       fields = '__all__'

class PraiaForm(forms.ModelForm):
    class Meta:
       model = Praia
       fields = '__all__'

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'telefone', 'nota', 'imagem', 'numero_visitas', 'sexo', 'faixa_etaria']