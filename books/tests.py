from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.

class Booktest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "test_test",
            author = "test_author",
            price = "26.00"
        )
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "test_test")
        self.assertEqual(f"{self.book.author}", "test_author")
        self.assertEqual(f"{self.book.price}", "26.00")
    
    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_test")
        self.assertTemplateUsed(response, "books/book_list.html")
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test_test")
        self.assertTemplateUsed(response, "books/detail.html")





"""    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
"""