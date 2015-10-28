from django.contrib import admin

# Register your models here.
from main.models import Author
from main.models import Book

admin.site.register(Author)
admin.site.register(Book)