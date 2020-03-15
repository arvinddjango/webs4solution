# Generated by Django 2.2.5 on 2019-09-22 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('blog_img', models.ImageField(upload_to='blog_imgage/')),
                ('blog_desc', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_created_date', models.DateTimeField(auto_now_add=True)),
                ('blog_updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
