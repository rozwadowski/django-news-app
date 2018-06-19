# -*- coding: utf-8 -*-
from django.contrib import admin

from news.models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)
