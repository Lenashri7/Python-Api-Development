from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "published_date": "2024-08-31",
            "isbn": "1234567890123",
            "page_count": 250,
            "cover": "http://example.com/test.jpg",
            "language": "English"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Test Book")

    def test_get_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_date="2024-08-31",
            isbn="1234567890123",
            page_count=250,
            cover="http://example.com/test.jpg",
            language="English"
        )
        url = reverse('book-detail', args=[book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_get_books_with_filters(self):
        Book.objects.create(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            published_date="1925-04-10",
            isbn="9780743273565",
            page_count=180,
            cover="http://example.com/gatsby.jpg",
            language="English"
        )
        Book.objects.create(
            title="Another Book",
            author="Another Author",
            published_date="2020-01-01",
            isbn="1234567890123",
            page_count=200,
            cover="http://example.com/another.jpg",
            language="English"
        )
        url = reverse('book-list-create') + '?author=F. Scott Fitzgerald&language=English'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Great Gatsby")

    def test_update_book(self):
        book = Book.objects.create(
            title="Old Title",
            author="Test Author",
            published_date="2024-08-31",
            isbn="1234567890123",
            page_count=250,
            cover="http://example.com/test.jpg",
            language="English"
        )
        url = reverse('book-detail', args=[book.id])
        updated_data = {
            "title": "New Title",
            "author": "Test Author",
            "published_date": "2024-08-31",
            "isbn": "1234567890123",
            "page_count": 250,
            "cover": "http://example.com/test.jpg",
            "language": "English"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "New Title")

    def test_delete_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_date="2024-08-31",
            isbn="1234567890123",
            page_count=250,
            cover="http://example.com/test.jpg",
            language="English"
        )
        url = reverse('book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the book was deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_nonexistent_book(self):
        url = reverse('book-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_nonexistent_book(self):
        url = reverse('book-detail', args=[999])
        updated_data = {
            "title": "New Title",
            "author": "Test Author",
            "published_date": "2024-08-31",
            "isbn": "1234567890123",
            "page_count": 250,
            "cover": "http://example.com/test.jpg",
            "language": "English"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_book(self):
        url = reverse('book-detail', args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
