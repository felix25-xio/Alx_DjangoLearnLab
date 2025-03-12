from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="books_all")

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token, name="obtain_auth_token"),
    path("books/", BookList.as_view(), name="book-list"),
    path("", include(router.urls)),
]