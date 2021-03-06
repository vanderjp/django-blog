from django.contrib import admin
from blogging.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInLine(admin.StackedInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]
