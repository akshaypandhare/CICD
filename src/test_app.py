# test_app.py
import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_endpoint(self):
        # Test the home endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the simple Flask API!", response.data)

    def test_health_check_endpoint(self):
        # Test the health endpoint
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Application is up and running smoothly.", response.data)

    def test_test_endpoint(self):
        # Test the test endpoint
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test endpoint is working", response.data)

if __name__ == '__main__':
    unittest.main()