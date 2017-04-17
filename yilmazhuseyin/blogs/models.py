from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from blogs.managers import BlogPostQuerySet

import markdown2


class _Month:
    """
    Month object that is used to render month on template
    """
    def __init__(self, dt):
        """
        month_dict = {'count': 3, 'month': u'2011-03-01'}
        """
        self.year = dt.year
        self.month = dt.month
        self.datetime = dt

    def __str__(self):
        return self.datetime.strftime("%B %Y")


class Blog(TimeStampedModel):
    name = models.CharField('Name of the Blog', max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=500, blank=True)
    tagline = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_index', kwargs={'blog_slug': self.slug})

    def get_date_list(self):
        return map(_Month, BlogPost.objects.filter(blog=self).get_date_list())


class Tag(models.Model):
    name = models.SlugField(max_length=500)
    blog = models.ForeignKey(Blog)

    class Meta():
        unique_together = (('name', 'blog'),)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self)


class Category(models.Model):
    name = models.SlugField(max_length=500)
    blog = models.ForeignKey(Blog)

    class Meta():
        unique_together = (('name', 'blog'),)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self)


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    published = models.BooleanField(default=True)
    teaser = models.TextField(blank=True)
    teaser_HTML = models.TextField(blank=True)
    content = models.TextField()
    content_HTML = models.TextField()
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)

    blog = models.ForeignKey(Blog)

    # objects = BlogPostManager()
    objects = BlogPostQuerySet.as_manager()

    class Meta():
        unique_together = (("slug", "blog"),)
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'blog_slug': self.blog.slug,
                                            'post_slug': self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return str(self)

    def save(self, *args, **kwargs):
        md = markdown2.Markdown()

        if not self.teaser:
            self.teaser = self.content

        self.teaser_HTML = md.convert(self.teaser)
        self.content_HTML = md.convert(self.content)

        super(BlogPost, self).save(*args, **kwargs)
