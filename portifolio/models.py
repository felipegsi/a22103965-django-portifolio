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
class SobreMim(models.Model):
    titulo = models.CharField(max_length=30)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]









########################################################
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=False, null=False)

    # imagem

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.ForeignKey(Autor,
                              on_delete=models.CASCADE,
                              related_name="artigo_autor")
    categoria = models.ManyToManyField(Categoria,
                                  related_name="artigos_categoria"
                                  )

    descricao = models.TextField(blank=False, null=False)
    # imagem
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
