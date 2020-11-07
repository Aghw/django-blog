from django.contrib import admin
from blogging.models import Post, Category

# # Define an inline class here
# class CategoryAdmin(admin.ModelAdmin):
#     pass

# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)

admin.site.register(Post)
admin.site.register(Category)
