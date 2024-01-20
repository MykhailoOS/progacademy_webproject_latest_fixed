from django.test import TestCase


# Create your tests here.

class ManagerTestCase(TestCase):
    """
    Unit tests for manager
    """
    def test_manager(self):
        response = self.client.get('/manager/')
        self.assertEqual(response.status_code, 200)
