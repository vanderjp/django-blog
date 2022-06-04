from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from django.template import loader
from blogging.models import Post


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date=None).order_by('-published_date')
    template_name = 'blogging/list.html'


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.queryset)

        context = {"object": post}
        return render(request, self.template_name, context)
