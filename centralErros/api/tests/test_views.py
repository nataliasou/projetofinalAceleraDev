from django.test import TestCase
from django.urls import reverse
from api.models import ErrorInstances
from accounts.models import User
from django.utils import timezone


class ErrorInstancesListViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            name='testuser1',
            email='testuser1@mail.com',
            password='1X<ISRUkw+tuK'
        )
        test_user2 = User.objects.create_user(
            name='testuser2',
            email='testuser2@mail.com',
            password='2HJ1vRV0Z&3iD'
        )

        test_user1.save()
        test_user2.save()

        number_of_errors = 12
        for error in range(number_of_errors):
            date_error = timezone.localtime()
            ErrorInstances.objects.create(
                title=f'Pagina não encontrada{error}',
                description='A página não foi encontrada!',
                origin='192.168.1.2',
                date=date_error,
                details='Detalhes são importantes',
                level='Warning',
                events=404,
                type_error='hom',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('pesquisa'))
        self.assertRedirects(response, '/login/?next=/api/pesquisa/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            email='testuser1@mail.com',
            password='1X<ISRUkw+tuK'
        )
        response = self.client.get(reverse('pesquisa'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1@mail.com')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'api/errorinstances_list.html')

        # Check if the pagination is working
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['errorinstances_list']) == 10)

        # Get second page and confirm it has (exactly) remaining 2 items
        response = self.client.get(reverse('pesquisa') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['errorinstances_list']) == 2)


class RegisterErrorViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            name='testuser1',
            email='testuser1@mail.com',
            password='1X<ISRUkw+tuK'
        )
        test_user2 = User.objects.create_user(
            name='testuser2',
            email='testuser2@mail.com',
            password='2HJ1vRV0Z&3iD'
        )

        test_user1.save()
        test_user2.save()

        number_of_errors = 12
        for error in range(number_of_errors):
            date_error = timezone.localtime()
            ErrorInstances.objects.create(
                title=f'Pagina não encontrada{error}',
                description='A página não foi encontrada!',
                origin='192.168.1.2',
                date=date_error,
                details='Detalhes são importantes',
                level='Warning',
                events=404,
                type_error='hom',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('register-error'))
        self.assertRedirects(response, '/login/?next=/api/cadastrar/')

    def test_uses_correct_template(self):
        login = self.client.login(
            email='testuser2@mail.com',
            password='2HJ1vRV0Z&3iD'
        )
        response = self.client.get(reverse('register-error'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/errorinstances_form.html')
