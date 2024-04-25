from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_success(self):
        email       =   "test@gmail.com"
        password    =   "12345"
        user        =   get_user_model().objects.create_user(
            email       =   email, 
            password    =   password,
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_user_email_normalized(self):
        sample_emails = [
            ['abc1@EXAMPLE.com', 'abc1@example.com'],
            ['Abc2@Example.com', 'Abc2@example.com'],
            ['ABC3@EXAMPLE.com', 'ABC3@example.com'],
            ['abc4@example.com', 'abc4@example.com']
        ]
        
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'aaa')
            self.assertEqual(user.email, expected)
            
    def test_new_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '12345')
            
    def test_create_superuser(self):
        email       =   "test@gmail.com"
        password    =   "12345"
        user        =   get_user_model().objects.create_superuser(
            email       =   email, 
            password    =   password,
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)