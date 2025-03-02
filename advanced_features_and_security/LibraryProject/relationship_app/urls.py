from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books
from .views import LibraryDetailView
from . import views


urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("admin/", views.admin_view, name="admin"),
    path("librarian/", views.librarian_view, name="librarian"),
    path("member/", views.member_view, name="member"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.add_book, name="add_book"),
    path("delete_book/", views.add_book, name="add_book"),
    path(
        "relationship_app/login",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "relationship_app/logout",
        LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
]