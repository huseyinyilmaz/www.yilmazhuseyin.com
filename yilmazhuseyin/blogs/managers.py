from django.db import models


class BlogPostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(published=True)

    def teaser(self):
        return self.published().defer('teaser_HTML')

    def content(self):
        return self.published().defer('content_HTML')

    def by_tag(self, tag):
        return self.published().filter(tags__name=tag)

    def by_category(self, category):
        return self.published().filter(categories__name=category)

    def get_date_list(self):
        """
        returns = [{'count': 3, 'month': u'2011-03-01'}...]
        """
        return self.datetimes('creation_date', 'month')\
            .order_by('creation_date')
