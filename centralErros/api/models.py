from django.db import models
import uuid
from accounts.models import User
from django.conf import settings


class ErrorInstances(models.Model):
    """
    This is all the date we need to register and see an error.
    Is related to :model: 'accounts.User'.
    """
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

    shelved = models.BooleanField(null=True, blank=True, default=False)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=50, help_text='Enter the error title',  default='')
    description = models.TextField(help_text='Describe the error', null=False, default='No description provided')
    origin = models.GenericIPAddressField('Describe the error origin',
                                 protocol='IPV4', max_length=39,
                                 default='0.0.0.0')
    date = models.DateTimeField(null=True, blank=True)
    details = models.TextField(help_text='Enter the error details', default='No description provided')

    def __str__(self):
        return self.level
