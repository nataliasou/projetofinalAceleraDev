from django.db import models

import uuid
from django.core import validators

from django.urls import reverse
from accounts.models import User


# class Log(models.Model):
#     # Class with error details
#     title = models.CharField(max_length=50, help_text='Enter the error title')
#     description = models.TextField(help_text='Describe the error')
#     origin = models.TextField(max_length=200,
#                               help_text='Describe the error origin')
#     date = models.DateTimeField(null=True, blank=True)
#     details = models.TextField(help_text='Enter the error details')
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         # Returns the url to access a detail record for this log.
#         return reverse('log-detail', args=[str(self.id)])


# class User(models.Model):
#     # Class representing the user model
#     name = models.CharField(max_length=50, help_text='Enter your name')
#     email = models.CharField(max_length=254,
#                              help_text='Enter your email',
#                              validators=[validators.EmailValidator()])
#     password = models.CharField(help_text='Enter you password',
#                                 max_length=50,
#                                 validators=[validators.MinLengthValidator(8)])
#
#     def __str__(self):
#         return self.name


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
    events = models.IntegerField(null=True, blank=True, help_text='Enter the error code')

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

    shelved = models.NullBooleanField(null=True, blank=True)
    user_id = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, help_text='Enter the error title')
    description = models.TextField(help_text='Describe the error')
    origin = models.TextField(max_length=200,
                              help_text='Describe the error origin')
    date = models.DateTimeField(null=True, blank=True)
    details = models.TextField(help_text='Enter the error details')

    #error = models.ForeignKey('Log', on_delete=models.SET_NULL, null=True)

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
