from django.test import TestCase, Client

class mainTest(TestCase):
    # Template Unit test
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'homepage.html')

    # Buatan Sendiri Unit test
    def test_header_content(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Qemul Olshop")

    def test_konten_information(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"Nama Aplikasi:")
        self.assertContains(response, "Nama:")
        self.assertContains(response, "Kelas:")
        

