from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User

from .models import App, SubApp
# Create your tests here.


class AppModelTest(TestCase):
    def test_App_created(self):
        # arrange
        firstApp: App = App(
            name="TestApp1", name_stringified=None, href="href-TestApp1")

        # act

        # assert
        self.assertIs(firstApp.name, "TestApp1")
        self.assertIs(firstApp.name_stringified, None)
        self.assertIs(firstApp.href, 'href-TestApp1')


class AppViewTest(TransactionTestCase):
    def setUp(self):
        App.objects.all().delete()

    def test_allApps_notLoggedIn(self):
        # arrange

        # act
        response = self.client.get('/')

        # assert
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/apps/accounts/login/?next=/')

    def test_allApps_LoggedIn(self):
        # arrange
        firstApp: App = App.objects.create(
            name="TestApp1", name_stringified=None, href="href-TestApp1")

        user: User = User.objects.create_user(
            username='test_user_for_tests',
            email='',
            password='test_user_for_tests'
        )

        self.client.force_login(user)

        # act
        response = self.client.get('/')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['apps'], [repr(firstApp)])
