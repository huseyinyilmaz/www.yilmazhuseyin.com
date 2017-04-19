from django.contrib import admin


from blogs.forms import BlogFormAdmin
from blogs.forms import BlogPostFormAdmin
from blogs.models import Blog
from blogs.models import BlogPost
from blogs.models import Tag


class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    form = BlogFormAdmin
    list_display = ('name', 'slug', 'title', 'created')
    list_select_related = True
    ordering = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('created', 'modified')
    save_on_top = True
    save_as = True
    search_fields = ['name', 'title']


class BlogPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    form = BlogPostFormAdmin
    list_display = ('title', 'slug', 'blog', 'created', 'published')
    list_filter = ('blog', 'published')
    list_select_related = True
    ordering = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created', 'modified')
    save_on_top = True
    save_as = True
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)
