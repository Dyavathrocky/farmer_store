from django.contrib import admin
from .models import Book , Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review

class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]

admin.site.register(Book, ReviewAdmin)