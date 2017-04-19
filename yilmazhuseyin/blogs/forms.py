from django import forms

from blogs.models import Blog
from blogs.models import BlogPost


class BlogFormAdmin(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'slug', 'title', 'description')


class BlogPostFormAdmin(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('published', 'blog', 'title', 'slug', 'content',
                  'teaser', 'categories', 'tags')

    def clean(self):
        if self.instance.id:
            try:
                self.changed_data.index('blog')
                raise forms.ValidationError(
                    "Blog of a Blog post cannot be changed")
            except ValueError:
                None

        super(BlogPostFormAdmin, self).clean()
        return self.cleaned_data
