from django import forms
from django.contrib import admin

from base.models import Category, ISBN , Book

class CategoryInline(admin.StackedInline):
    model = Category
    extra = 0

class BookAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'user')
    
    def get_queryset(self, request):
        # Get the currently logged-in user's ID
        user_id = request.user.id
        # Filter the queryset to include only books belonging to the logged-in user
        queryset = super().get_queryset(request).filter(user_id=user_id)
        return queryset


admin.site.register(Book , BookAdmin)
admin.site.register(ISBN)
admin.site.register(Category)