from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('O e-mail é obrigatório')

        usuario = self.model(email=email)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(email, password=password)
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario
