# Generated by Django 2.2.5 on 2019-11-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0023_getstartphp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_sort_desc', models.CharField(max_length=552)),
                ('project_name', models.CharField(max_length=151)),
                ('project_name_app', models.CharField(max_length=151)),
                ('project_technology_used1', models.CharField(blank=True, max_length=51)),
                ('project_technology_used2', models.CharField(blank=True, max_length=51)),
                ('project_technology_used3', models.CharField(blank=True, max_length=51)),
                ('project_technology_used4', models.CharField(blank=True, max_length=51)),
                ('project_technology_used5', models.CharField(blank=True, max_length=51)),
                ('project_technology_used6', models.CharField(blank=True, max_length=51)),
                ('project_desc', models.TextField()),
                ('project_img', models.ImageField(upload_to='Project_Img/')),
            ],
        ),
    ]