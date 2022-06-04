from blogging.views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]

