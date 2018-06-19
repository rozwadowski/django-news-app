# -*- coding: utf-8 -*-
from django.db import models


	
class Category(models.Model):
	name = models.CharField('Nazwa kategorii', max_length=255)
	slug = models.SlugField('Odnośnik', max_length=255, unique=True)
	icon = models.ImageField('Ikonka Kategorii', upload_to='icons', blank=True)

	class Meta:
		verbose_name = "Kategoria"
		verbose_name_plural = "Kategorie"
	
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return str(self.name)
	
	
class News(models.Model):
    title = models.CharField('Tytuł', max_length=255)
    slug = models.SlugField('Odnośnik', max_length=255, unique=True)
    text = models.TextField(verbose_name='Treść')
    posted_date = models.DateTimeField('Data dodania', auto_now_add=False)
    tag = models.ManyToManyField(Category, verbose_name='Kategorie')
    pic = models.ImageField('Obrazek', upload_to='media', blank=True)
    pic_caption = models.CharField(default='Podpis obrazka', max_length=255)
	
    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"

    def __unicode__(self):
        return self.title
    def __str__(self):
        return str(self.title)
	
    def get_tag(self):
        return self.tag
	