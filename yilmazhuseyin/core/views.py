from django.shortcuts import render
from blogs import models


def index(request):
    context = {'page': 'index',
               'blogs': models.Blog.objects.all()}
    return render(request,
                  'core/index.html',
                  context=context)
