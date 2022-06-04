from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, permissions

from blogging.models import Post
from blogging.serializers import PostSerializer, UserSerializer


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.queryset)

        context = {"object": post}
        return render(request, self.template_name, context)


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date=None).order_by("-published_date")
    template_name = "blogging/list.html"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
