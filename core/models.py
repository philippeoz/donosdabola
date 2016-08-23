from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser


class Cliente(AbstractBaseUser):
    """
    Classe de usuário customizada, utilizando/extendendo AbstractUser
    """
    nome = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=True)
    telefone = models.CharField(max_length=15)
    cpf_cnpj = models.CharField(max_length=15)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('cliente_update', kwargs={'pk': self.pk})


class Campo(models.Model):
    """ """
    nome = models.CharField(null = False, unique=True,max_length=20)
    descricao = models.TextField()
    horario_disponivel_de = models.TimeField(default=timezone.now)
    horario_disponivel_ate = models.TimeField(default=timezone.now)
    valor_hora = models.FloatField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('dashboard')


class Reserva(models.Model):
    """docstring for Reserva"""
    campo = models.ForeignKey(Campo, max_length=20)

    reservado_por = models.ForeignKey(Cliente)

    data_da_reserva = models.DateField(default=timezone.now)

    reservado_de = models.TimeField(default=timezone.now)

    reservado_ate = models.TimeField(default=timezone.now)

    def __unicode__(self):
        return u'%s - %s' % (self.campo.nome, self.reservado_por.username)

    def get_absolute_url(self):
        return reverse('reserva-detail', kwargs={'pk': self.pk})


