from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse , resolve
from .views import SignupView
from .forms import CustomUserCreationForm

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

class SignupViewTest(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def Signuptest(self):
        self.assertContains(self.response, "Signup")
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertNotContains(self.response , "hi this is ")

    
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup")
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)
