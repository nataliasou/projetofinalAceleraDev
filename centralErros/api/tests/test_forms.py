from django.test import TestCase
from api.forms import RegisterErrorForm


class RegisterErrorFormTest(TestCase):

    def test_form_title_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['title'].label == None
            or form.fields['title'].label == 'Titulo')

    def test_form_description_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['description'].label == None
            or form.fields['description'].label == 'Descrição')

    def test_form_origin_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['origin'].label == None
            or form.fields['origin'].label == 'Origem')

    def test_form_date_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['date'].label == None
            or form.fields['date'].label == 'Data')

    def test_form_details_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['details'].label == None
            or form.fields['details'].label == 'Detalhes')

    def test_form_level_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['level'].label == None
            or form.fields['level'].label == 'Nivel')

    def test_form_events_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['events'].label == None
            or form.fields['events'].label == 'Eventos')

    def test_form_type_error_field_label(self):
        form = RegisterErrorForm(user_id=1)
        self.assertTrue(
            form.fields['type_error'].label == None
            or form.fields['type_error'].label == 'Tipo')
