from django.test import TestCase

# Test created for models.py
from accounts.models import User, UserManager


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Data to use by all tests methods
        User.objects.create(
            name='Natalia',
            email='nat@gmail.com',
            is_active=True,
            staff=False,
            admin=False
        )

    # Testing the labels
    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_users_name(self):
        user_name = User.objects.get(id=1)
        self.assertEquals(user_name.get_full_name(), 'Natalia')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email address')

    def test_email_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

    def test_users_email(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.get_short_name(), 'nat@gmail.com')

    def test_is_active_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'is active')

    def test_staff_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('staff').verbose_name
        self.assertEquals(field_label, 'staff')

    def test_admin_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('admin').verbose_name
        self.assertEquals(field_label, 'admin')
