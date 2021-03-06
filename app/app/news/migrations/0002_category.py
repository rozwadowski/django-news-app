# Generated by Django 2.0.6 on 2018-06-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa kategorii')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')),
                ('icon', models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka Kategorii')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
    ]
