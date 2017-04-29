from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect

from blogs import models


def index(request):
    context = {'page': 'index',
               'blogs': models.Blog.objects.all()}
    return render(request,
                  'core/index.html',
                  context=context)


def about(request):
    """Because old version of blog had that path."""
    return redirect(reverse('core-index'))
