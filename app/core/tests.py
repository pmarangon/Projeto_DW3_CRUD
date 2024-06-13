from django.test import TestCase
from .views import home_view

class HomeViewTest(TestCase):

    def test_home_view_(self):
        context_test = {
            'home': True,
            'agenda': False,
        }

        response = home_view(request=self.client.get('/home/'))
        context_renderizado = response.context_data

        self.assertEqual(context_test, context_renderizado)

