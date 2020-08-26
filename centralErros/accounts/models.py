from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        Create a token to relate a user.
    """
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """
        Creates and saves a User with the given name, email and password.
        """
        if not email:
            raise ValueError('Você tem que ter um email!')

        if not name:
            raise ValueError('Digite seu nome!')

        if not password:
            raise ValueError('Você tem que ter uma senha!')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, name, email, password):
        """
        Creates and saves a staff user with the given name, email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """
        Creates and saves a superuser with the given name, email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    All the data needed for the user profile.
    """
    objects = UserManager()
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Nome'
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Return the user's name.
        """
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        """
        Return the user's email.
        """
        # The user is identified by their email address
        return self.email

    def get_user(self, user_id):
        """
        Return the user's id.
        """
        try:
            return self.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class UsersEmail(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
