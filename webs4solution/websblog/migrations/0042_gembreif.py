# Generated by Django 2.2.5 on 2019-12-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0041_gemtitledesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeMBreif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_brief_title', models.CharField(max_length=101)),
                ('gem_brief_desc', models.TextField()),
                ('gem_brief_title1', models.CharField(max_length=101)),
                ('gem_brief_desc1', models.TextField()),
            ],
        ),
    ]
