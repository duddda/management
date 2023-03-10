import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from reversion import revisions as reversion
from .usuario_manager import UsuarioManager
from ..utils import CharUpperField, CharLowerField, mkpass, send_mail_new_password

@reversion.register()
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objects = UsuarioManager()

    nome = CharUpperField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    email = CharLowerField('Endereço de e-mail', max_length=255, unique=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True, default=None)
    is_active = models.BooleanField(verbose_name='Ativo?', default=True)
    is_superuser = models.BooleanField(verbose_name='Super usuário?', default=False)
    is_first_login = models.BooleanField(verbose_name='Primeiro Login?', default = False)

    USERNAME_FIELD = 'email'

    def is_administrador(self):
        if self.is_superuser:
            return True

    @property
    def get_full_name(self):
        if self.nome:
            return self.nome
        return self.email

    @property
    def get_short_name(self):
        if self.nome:
            letters = self.nome.split()
            return letters[0] + " " + letters[len(letters)-1]
        return self.email.split()

    @property
    def get_last_name(self):
        if self.nome:
            letters = self.nome.split()
            return letters[len(letters)-1]
        return ""

    def has_group(self, group_name):
        group =  Group.objects.get(name=group_name)
        return group in self.groups.all()

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return  self.nome

    @property
    def is_staff(self):
        return self.is_active

    def save(self, *args, **kwargs):
        print('aqui')
        if not self.pk and not self.password:
            print('aqui')
            password = self.gerar_nova_senha()
            self.set_password(password)
            send_mail_new_password(self,password)
        super(Usuario, self).save(*args, **kwargs)

    def gerar_nova_senha(self):
        nova_senha = mkpass(8)
        self.set_password(nova_senha)

        return nova_senha


    class Meta:
        app_label = 'login'
        db_table = app_label + '_usuario'
