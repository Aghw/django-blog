from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import loader
from blogging.models import Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from blogging.serializers import UserSerializer, GroupSerializer
from blogging.serializers import PostSerializer, CategorySerializer
from datetime import datetime, timedelta


class BlogListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]