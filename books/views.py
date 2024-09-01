
from rest_framework import status, generics
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author')
        published_date = self.request.query_params.get('published_date')
        language = self.request.query_params.get('language')
        
        if author:
            queryset = queryset.filter(author__icontains=str(author))
        if published_date:
            queryset = queryset.filter(published_date=str(published_date))
        if language:
            queryset = queryset.filter(language__icontains=str(language))
        
        return queryset

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
