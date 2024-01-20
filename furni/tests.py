from django.test import TestCase


# Create your tests here.

class FurniTestCase(TestCase):
    """
    Tests for Furni
    """
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
