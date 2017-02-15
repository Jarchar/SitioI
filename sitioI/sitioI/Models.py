from django.db import models
from django.contrib.auth.models import(
        BaseUserManager, AbstractBaseUser
        )

class AdministrarUsr(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError('Se requiere un email para el usuario')
        user = self.model(
                email.self.normalize_email(email),
                nombre=nombre,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,nombre,password):
        user=self.create_user(
                email,
                password=password,
                nombre=nombre,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email=models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True,
        )
    nombre=models.CharField(max_length=200)
    is_active=models.BooleanField(defualt=True)
    is_admin=models.BooleanField(default=False)

    objects= AdministrarUsr()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['nombre']

    def get_full_name(self):
        return self.nombre
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def had_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
