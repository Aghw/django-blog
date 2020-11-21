from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms

from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from blogging.forms import BlogPostForm

class BlogListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )


class BlogDetailView(DetailView):
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None)


class BlogAddView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/add.html"

def add_model(request):
    
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            redirect('/')
        else:
            return render(request, "blogging/add.html", {'form': form})
    else:
        form = BlogPostForm()

        return render(request, "blogging/add.html", {'form': form})