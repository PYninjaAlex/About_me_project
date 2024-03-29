from django.test import TestCase


class ViewsTests(TestCase):
    def test_main_page(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        response = self.client.get("/database/")
        self.assertEqual(response.status_code, 200)
