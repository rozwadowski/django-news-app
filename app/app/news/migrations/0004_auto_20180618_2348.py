# Generated by Django 2.0.6 on 2018-06-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='posted_date',
            field=models.DateTimeField(verbose_name='Data dodania'),
        ),
    ]