from django.test import TestCase

# Test created for models.py
from api.models import ErrorInstances


class ErrorInstancesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        ErrorInstances.objects.create(
            level='Critical',
            events=1000,
            type_error='hom',
            shelved=False,
            title='Erro Teste',
            description='blablalablablablablablablabla fiffifififi fofofofofo',
            origin='Teste',
            date='2020-07-05 14:30:43',
            details='Detalhes são importantes',
        )

    def test_level_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('level').verbose_name
        self.assertEquals(field_label, 'level')

    def test_level_max_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('level').max_length
        self.assertEquals(max_length, 20)

    def test_level_choices(self):
        errorInstances = ErrorInstances.objects.get()
        self.assertEquals(errorInstances.level, 'Critical')

    def test_events_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('events').verbose_name
        self.assertEquals(field_label, 'events')

    def test_type_error_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('type_error').verbose_name
        self.assertEquals(field_label, 'type error')

    def test_type_error_max_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('type_error').max_length
        self.assertEquals(max_length, 20)

    def test_type_error_choices(self):
        errorInstances = ErrorInstances.objects.get()
        self.assertEquals(errorInstances.type_error, 'hom')

    def test_shelved_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('shelved').verbose_name
        self.assertEquals(field_label, 'shelved')

    def test_title_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_description_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_origin_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('origin').verbose_name
        self.assertEquals(field_label, 'origin')

    def test_origin_length(self):
        errorInstances = ErrorInstances.objects.get()
        max_length = errorInstances._meta.get_field('origin').max_length
        self.assertEquals(max_length, 200)

    def test_date_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_details_label(self):
        errorInstances = ErrorInstances.objects.get()
        field_label = errorInstances._meta.get_field('details').verbose_name
        self.assertEquals(field_label, 'details')

    def test_if_str_is_returning_level(self):
        errorInstances = ErrorInstances.objects.get()
        expected_object_name = f'{errorInstances.level}'
        self.assertEquals(expected_object_name, str(errorInstances))
