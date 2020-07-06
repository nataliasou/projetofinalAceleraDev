from django.test import TestCase

# Test created for models.py
from api.models import Log, User, ErrorInstances, Group

class LogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        Log.objects.create(title='Erro Teste', description='blablalablablablablablablabla fififififififi fofofofofo', origin='Teste', date='2020-07-05', details='Detalhes são importantes')

    #Testing the labels
    def test_title_label(self):
        log = Log.objects.get(id=1)
        field_label = log._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        log = Log.objects.get(id=1)
        field_label = log._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_origin_label(self):
        log = Log.objects.get(id=1)
        field_label = log._meta.get_field('origin').verbose_name
        self.assertEquals(field_label, 'origin')

    def test_date_label(self):
        log = Log.objects.get(id=1)
        field_label = log._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_details_label(self):
        log = Log.objects.get(id=1)
        field_label = log._meta.get_field('details').verbose_name
        self.assertEquals(field_label, 'details')

    # Testing the limits
    def test_title_max_length(self):
        log = Log.objects.get(id=1)
        max_length = log._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)
   #TA FALHANDO PQ AINDA NAO MCHI NO URL
    """def test_get_absolute_url(self):
        log = Log.objects.get(id=1)
        self.assertEquals(log.get_absolute_url(), '/api/log/1')"""

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        User.objects.create(name='Arlindo', email='arlindo@gmail.com', password='12345678')

    #Testing the labels
    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

    def test_password_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length, 50)
"""  COMO TESTAR O VALIDATORS????????????????????????
    def test_password_validators(self):
        user = User.objects.get(id=1)
        validators = user._meta.get_field('password').validators
        self.assertEquals(validators, )"""


class ErrorInstancesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        ErrorInstances.objects.create(level='Critical', events=1000, type_error='hom', shelved=False)

    # Testing the labels
    def test_level_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('level').verbose_name
        self.assertEquals(field_label, 'level')

    def test_events_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('events').verbose_name
        self.assertEquals(field_label, 'events')

    def test_type_error_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('type_error').verbose_name
        self.assertEquals(field_label, 'type error')

    def test_shelved_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('shelved').verbose_name
        self.assertEquals(field_label, 'shelved')

    # Testing max_length
    def test_level_max_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('level').max_length
        self.assertEquals(max_length, 20)

    def test_type_error_max_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('type_error').max_length
        self.assertEquals(max_length, 20)

    # Testing the choices
    """def test_level_choices(self):
        errorInstances = ErrorInstances.objects.get()
        choices = errorInstances._meta.get_field('level').choices
        self.assertEquals(choices, 'level')
    def test_type_error_choices(self):
        errorInstances = ErrorInstances.objects.get()
        choices = errorInstances._meta.get_field('type_error').choices
        self.assertEquals(choices, 'type error')
"""


class GroupTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        Group.objects.create(name='Teste')

    # Testing the labels
    def test_name_label(self):
        group = Group.objects.get(id=1)
        field_label = group._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Testing the labels
    def test_name_max_length(self):
        group = Group.objects.get(id=1)
        max_length = group._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)