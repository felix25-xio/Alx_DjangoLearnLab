from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]
    search_fields = ["title", "author"]
    list_filter = ["publication_year"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)