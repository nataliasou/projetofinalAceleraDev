from django.test import TestCase
from accounts.forms import (
    RegisterForm,
    UserAdminCreationForm,
    UsersForm,
    LoginForm
)


class UsersFormTest(TestCase):
    def test_form_email_char_field(self):
        form = UsersForm()
        self.assertTrue(
            form.fields['email'].label == None
            or form.fields['email'].label == 'Email address')


class LoginFormTest(TestCase):
    def test_form_email_char_field(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['email'].label == None
            or form.fields['email'].label == 'Email')

    def test_form_password_char_field(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['password'].label == None
            or form.fields['password'].label == 'Senha')


class RegisterFormTest(TestCase):
    def test_form_password1_char_field(self):
        form = RegisterForm()
        self.assertTrue(
            form.fields['password1'].label == None
            or form.fields['password1'].label == 'Senha')

    def test_form_password2_char_field(self):
        form = RegisterForm()
        self.assertTrue(
            form.fields['password2'].label == None
            or form.fields['password2'].label == 'Confirmação de senha')

    def test_form_name_char_field(self):
        form = RegisterForm()
        self.assertTrue(
            form.fields['name'].label == None
            or form.fields['name'].label == 'Name')

    def test_form_email_char_field(self):
        form = RegisterForm()
        self.assertTrue(
            form.fields['email'].label == None
            or form.fields['email'].label == 'Email address')


class UserAdminCreationFormTest(TestCase):
    def test_form_password1_char_field(self):
        form = UserAdminCreationForm()
        self.assertTrue(
            form.fields['password1'].label == None
            or form.fields['password1'].label == 'Senha')

    def test_form_password2_char_field(self):
        form = UserAdminCreationForm()
        self.assertTrue(
            form.fields['password2'].label == None
            or form.fields['password2'].label == 'Confirmação de senha')

    def test_form_name_char_field(self):
        form = UserAdminCreationForm()
        self.assertTrue(
            form.fields['name'].label == None
            or form.fields['name'].label == 'Name')

    def test_form_email_char_field(self):
        form = UserAdminCreationForm()
        self.assertTrue(
            form.fields['email'].label == None
            or form.fields['email'].label == 'Email address')
