from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, _("Пользователь")),
        (ADMIN, _("Администратор")),
    )


class User(AbstractBaseUser):
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    username = None

    first_name = models.CharField(
        max_length=64,
        verbose_name="Имя",
        help_text="Введите имя (максимум 64 символа)",
    )

    last_name = models.CharField(
        max_length=64,
        verbose_name="Фамилия",
        help_text="Введите фамилию (максимум 64 символа)",
    )

    email = models.EmailField(
        "email address",
        unique=True,
        help_text="Укажите электронную почту",
    )

    phone = PhoneNumberField(
        verbose_name="Телефон для связи",
        help_text="Укажите телефон для связи",
    )

    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите  роль пользователя",
    )

    is_active = models.BooleanField(
        verbose_name="Флаг активности аккаунта",
        help_text="Укажите, активен ли аккаунт",
    )

    image = models.ImageField(
        upload_to='django_media/users/',
        verbose_name="Аватарка",
        help_text="Выберите свой аватар",
        null=True,
        blank=True,
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
