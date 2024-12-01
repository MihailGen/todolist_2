from django.contrib import admin
from .models import Task, Comment, Tag, Category


class CommentInline(admin.TabularInline):
    model = Comment


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'due_date', 'category')
    search_fields = ('name', 'description', 'category')
    list_filter = ('due_date', 'author', 'category')


    inlines = [
        CommentInline,
    ]

admin.site.register(Tag)