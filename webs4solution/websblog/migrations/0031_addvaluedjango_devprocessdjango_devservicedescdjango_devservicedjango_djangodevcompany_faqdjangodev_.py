# Generated by Django 2.2.5 on 2019-11-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0030_phpdevcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddValueDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_value_django_title', models.CharField(max_length=51)),
                ('add_value_django_img', models.ImageField(upload_to='Django_img/add_value')),
                ('add_value_django_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DevProcessDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_django_title', models.CharField(max_length=51)),
                ('dev_django_img', models.ImageField(upload_to='Django_img/')),
                ('dev_django_desc', models.TextField()),
                ('dev_django_img_screen', models.ImageField(upload_to='Django_img/laptop_screen')),
            ],
        ),
        migrations.CreateModel(
            name='DevServiceDescDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_service_django_desc', models.CharField(max_length=551)),
            ],
        ),
        migrations.CreateModel(
            name='DevServiceDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_service_django_title', models.CharField(max_length=51)),
                ('dev_servic_django_img', models.ImageField(upload_to='Django_img/dev_service')),
            ],
        ),
        migrations.CreateModel(
            name='DjangoDevCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_dev_title', models.CharField(max_length=51)),
                ('django_dev_desc', models.TextField()),
                ('django_dev_img', models.ImageField(upload_to='Django_img/django_dev_company')),
            ],
        ),
        migrations.CreateModel(
            name='FaqDjangoDev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=250)),
                ('answer1', models.TextField()),
                ('question2', models.CharField(max_length=250)),
                ('answer2', models.TextField()),
                ('question3', models.CharField(max_length=250)),
                ('answer3', models.TextField()),
                ('question4', models.CharField(max_length=250)),
                ('answer4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GetStartDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_title', models.CharField(max_length=251)),
                ('django_desc', models.CharField(max_length=551)),
                ('django_img1', models.ImageField(upload_to='django_ico_img/')),
                ('django_img_title1', models.CharField(max_length=151)),
                ('django_img2', models.ImageField(upload_to='django_ico_img/')),
                ('django_img_title2', models.CharField(max_length=151)),
                ('django_img3', models.ImageField(upload_to='django_ico_img/')),
                ('django_img_title3', models.CharField(max_length=151)),
                ('django_img4', models.ImageField(upload_to='django_ico_img/')),
                ('django_img_title4', models.CharField(max_length=151)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionExpertiseDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sol_exper_django_title', models.CharField(max_length=51)),
                ('sol_exper_django_img', models.ImageField(upload_to='Django_img/solution_expertise')),
            ],
        ),
    ]
