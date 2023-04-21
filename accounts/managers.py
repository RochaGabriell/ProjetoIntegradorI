from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Gerenciador de modelo de usuário personalizado em que o e-mail é o identificador 
    exclusivo para autenticação em vez de nomes de usuários.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Crie e salve um usuário com o e-mail e a senha fornecidos.
        """
        if not email:
            raise ValueError(_("O e-mail deve ser definido"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Crie e salve um SuperUser com o e-mail e a senha fornecidos.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("O superusuário deve ter is_superuser=True."))
        return self.create_user(email, password, **extra_fields)