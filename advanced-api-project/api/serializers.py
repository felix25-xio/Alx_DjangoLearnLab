from rest_framework import serializers
from .models import Book, Author
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the instance of the Book instance which include title, publication_year and author
    """

    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate(self, data):
        """
        Serializer method to validate and ensure that the year is not in the future
        """
        if data["publication_year"] > (date.today()).year:
            print((date.today()).year)
            raise serializers.ValidationError(
                "The publication should not be in the future"
            )
        return data


class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)  # This handles the one-to-many relationship between the Author and Book model

    class Meta:
        model = Author
        fields = ["id", "name", "books"]