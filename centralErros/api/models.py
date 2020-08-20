from django.db import models
import uuid
from accounts.models import User
from django.conf import settings


class ErrorInstances(models.Model):
    # Class representing the Error Event model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this error")
    LEVEL_STATUS = (
        ('Critical', 'Critical'),
        ('Debug', 'Debug'),
        ('Error', 'Error'),
        ('Warning', 'Warning'),
        ('Info', 'Info'),
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_STATUS,
        blank=True,
        default='Error',
        help_text='Choose the error level'
    )
    events = models.IntegerField(
        null=True,
        blank=True,
        help_text='Enter the error code'
    )
    TYPE_ERROR_STATUS = (
        ('dev', 'desenvolvedor'),
        ('hom', 'homolgação'),
        ('prod', 'produção'),
    )

    type_error = models.CharField(max_length=20,
                                  choices=TYPE_ERROR_STATUS,
                                  blank=True,
                                  default='dev',
                                  help_text='Choose the error type'
                                  )

    shelved = models.NullBooleanField(null=True, blank=True, default=False)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=50, help_text='Enter the error title')
    description = models.TextField(help_text='Describe the error')
    origin = models.TextField(max_length=200,
                              help_text='Describe the error origin')
    date = models.DateTimeField(null=True, blank=True)
    details = models.TextField(help_text='Enter the error details')

    def __str__(self):
        return self.level


class Group(models.Model):
    # Class representing the group model
    name = models.CharField(max_length=20, help_text='Enter the group name')

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    # Representing group user
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
