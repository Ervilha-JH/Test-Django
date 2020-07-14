from django.db import models
from django.contrib.auth.models import User
# Meu Modelo

class Personagem(models.Model):

    name = models.CharField(max_length = 100)
    descricao_fisica = models.CharField(max_length = 200)
    preludio = models.TextField()
    refugio = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()
    vivo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'personagem'
