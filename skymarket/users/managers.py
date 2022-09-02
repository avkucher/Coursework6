from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        """
        функция создания пользователя — в нее мы передаем обязательные поля
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.role = "user"
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем
        админинстратора это можно сделать с помощью команды createsuperuser
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.role = 'admin'
        user.save(using=self._db)

        return user
