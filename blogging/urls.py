from django.urls import path
from blogging.views import BlogListView, BlogDetailView
from blogging.views import add_model

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("add/", add_model, name="add_post")
]
