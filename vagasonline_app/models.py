from django.db import models
from django.utils.timezone import now

# Create your models here.
class Candidato(models.Model):
    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=150, default="Endereço não informado")
    email = models.EmailField(unique=True, default="defaul@email.com")
    telefone = models.CharField(max_length=30, default="Telefone não informado")
    nascimento = models.DateField()
    idade= models.IntegerField(default=0)
    genero = models.CharField(max_length=100, default="Genero não informado")
    curriculo = models.FileField(upload_to="curriculos", blank=True, null=True)
    vaga = models.CharField(max_length=100, default="Não informado")
    add_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.nome[:40]