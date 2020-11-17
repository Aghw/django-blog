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
    d10 = timedelta(10)
    now = datetime.now()
    queryset = Post.objects.all().order_by('-published_date').filter(published_date__gt=(now - d10))


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
