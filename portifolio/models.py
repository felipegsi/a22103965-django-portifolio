from django.db import models


# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport,
                               on_delete=models.CASCADE,
                               related_name="departures")
    destination = models.ForeignKey(Airport,
                                    on_delete=models.CASCADE,
                                    related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=20)
    flights = models.ManyToManyField(
        Flight,
        blank=True,
        related_name='passengers'
    )

    def __str__(self):
        return self.name


############alterar sobre mim para cadeiras##################
class SobreMim(models.Model):  # sera substituido pela cadeira
    titulo = models.CharField(max_length=30)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link_linkedin = models.URLField()

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    DIFICULDADE_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
        ('profissional', 'Profissional'),
    ]
    nome = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=20, choices=DIFICULDADE_CHOICES, blank=True, null=True)
    data_inicio = models.DateField()
    data_conclusao = models.DateField()
    descricao = models.TextField()
    ranking = models.PositiveIntegerField(
        choices=((1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas'))
        , blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)

    # Outros atributos do projeto aqui

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    SEMESTER_CHOICES = (
        ('1', '1º semestre'),
        ('2', '2º semestre'),
        ('3', '3º semestre'),
        ('4', '4º semestre'),
        ('5', '5º semestre'),
        ('6', '6º semestre'),
    )

    nome = models.CharField(max_length=100)
    ano_letivo_frequentado = models.PositiveIntegerField()
    semestre = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    creditos_ects = models.PositiveIntegerField()
    topicos_abordados = models.TextField()
    ranking = models.PositiveIntegerField(
        choices=((1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas'))
    )
    professores = models.ManyToManyField(Pessoa)
    projetos_realizados = models.ManyToManyField(Projeto)
    imagem = models.ImageField(upload_to='cadeiras/', blank=True, null=True)
    nota = models.PositiveIntegerField()
    departamento = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    descricao_cadeira = models.TextField()

    def __str__(self):
        return self.nome


########################################################

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=False, null=False)
    imagem = models.ImageField(upload_to='categorias/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=30)
    biografia = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria, related_name="artigos")
    descricao = models.TextField(blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='artigos/', blank=True, null=True)
    visitas = models.PositiveIntegerField(default=0)
    conteudo = models.TextField(default='your_default_value', blank=False, null=False)  # Add the default parameter

    def __str__(self):
        return self.titulo


class Contato(models.Model):
    ASSUNTO_CHOICES = [
        ('duvida', 'Dúvida'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    assunto = models.CharField(max_length=20, choices=ASSUNTO_CHOICES)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome


class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Praia(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
