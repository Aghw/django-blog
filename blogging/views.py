from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime, timedelta

class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    queryset = Post.objects.exclude(published_date__exact=None)
