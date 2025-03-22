from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

# Please and please don't use this code it's not satisfying, I am yet to understand test
# I did thid to beat the deadline, I will come to it later and rectify it.
# Don't rely on it please.


class BookTest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Introduction to Django",
            publication_year=2023,
            author=Author.objects.create(name="Alinda Fortunate"),
        )
        self.url = reverse("create-book")

    def test_create_book(self):
        """
        Test method to ensure that we can create a book
        """
        data = {
            "title": "Introduction to Django",
            "publication_year": 2023,
            "author": 1,
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Introduction to Django")

    def test_authenticated_user(self):
        self.client.login(username="alinda", password="secret")
        pass