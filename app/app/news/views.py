# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from news.models import *


def index(request):
    news = News.objects.all().order_by('-posted_date',)
    tags = Category.objects.all().order_by('name',)
    
    #for i in news.objects.get(id=1)
    #for i in news.objects.all():
    tag = []
    for n in news:
        tmp = []
        for i in News.objects.get(title=str(n)).tag.all().order_by('name',):
            tmp.append(str(i))
        tag.append(tmp)
    
    return render_to_response('index.html',
            {'news': news,'tags': tags,'tag': tag},
            RequestContext(request))