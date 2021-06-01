from django.test import TestCase
from django.contrip.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.asserEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email reises error"""
        with self.asserRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTure(user.is_superuser)
        self.assertTrue(user.is_staff)