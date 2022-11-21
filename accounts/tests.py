from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="test" , email="test@test.com", password="testpass987"
        )
        self.assertEqual(user.username , "test")
        self.assertEqual(user.email , "test@test.com")
        self.assertEqual(user.password , "testpass987")

    def test_create_superuser(self):
            User = get_user_model()
            sup_user = User.objects.create_superuser(
            username="test" , email="test@test.com", password="testpass987" 
        )
            self.assertEqual(sup_user.username , "test")
            self.assertEqual(sup_user.email , "test@test.com")
            #self.assertEqual(sup_user.password , "testpass987")
            self.assertTrue(sup_user.is_active),
            self.assertTrue(sup_user.is_staff),
            self.assertTrue(sup_user.is_superuser)

