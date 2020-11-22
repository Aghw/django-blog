from django.forms import ModelForm
from blogging.models import Post


class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        # fields = "__all__"
