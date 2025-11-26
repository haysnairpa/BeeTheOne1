import unittest
from BeeTheOne.sia import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Set up test client
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'BeeTheOne', result.data)

    def test_login_page_get(self):
        result = self.app.get('/login')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Login', result.data)

    def test_login_page_post_invalid(self):
        result = self.app.post('/login', data=dict(username='bad', password='user'))
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Invalid credentials', result.data)

    def test_login_page_post_valid_and_honey_access(self):
        # Login with admin credentials
        result = self.app.post('/login', data=dict(username='admin', password='honey'), follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Dashboard', result.data)

        # Access the /honey page (requires login)
        honey_result = self.app.get('/honey')
        self.assertEqual(honey_result.status_code, 200)
        self.assertIn(b'Jenis-Jenis Madu', honey_result.data)

    def test_honey_page_requires_login(self):
        # Access /honey without login should redirect
        result = self.app.get('/honey', follow_redirects=True)
        self.assertIn(b'Login', result.data)

    def test_inventory_page_requires_login(self):
        # Access /inventory without login should redirect
        result = self.app.get('/inventory', follow_redirects=True)
        self.assertIn(b'Login', result.data)

if __name__ == "__main__":
    unittest.main()
