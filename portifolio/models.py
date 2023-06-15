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
        null=True,
        blank=True,
        related_name='passengers'
    )

    def __str__(self):
        return self.name


class Conta(models.Model):
    repo_github = models.CharField(max_length=100)
    pythonanywhere = models.CharField(max_length=100)

    def __str__(self):
        return f"Conta - Repo GitHub: {self.repo_github}, PythonAnywhere: {self.pythonanywhere}"


class Area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    areas_interesse = models.ManyToManyField(Area)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    data = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='artigos/', null=True, blank=True)
    link = models.URLField()
    comentarios = models.ManyToManyField('Comentario', blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
