from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

# Define an inline class here
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    empty_value_display = '-empty-'
    fields = ('name', 'description')

    inlines = [
        CategoryInline,
    ]
    exclude = ('posts',)

    def view_name(self, obj):
        return obj.name

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # actions_on_bottom = True; actions_on_top = False
    actions_on_bottom = True

    inlines = [
        CategoryInline,
    ]
