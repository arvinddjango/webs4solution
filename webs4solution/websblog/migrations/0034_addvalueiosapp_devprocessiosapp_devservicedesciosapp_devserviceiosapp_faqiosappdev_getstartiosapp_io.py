# Generated by Django 2.2.5 on 2019-12-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0033_addvaluelaravel_addvaluewordpress_devprocesslaravel_devprocesswordpress_devservicedesclaravel_devser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddValueIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_value_iosapp_title', models.CharField(max_length=51)),
                ('add_value_iosapp_img', models.ImageField(upload_to='iosapp_img/add_value')),
                ('add_value_iosapp_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DevProcessIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_iosapp_title', models.CharField(max_length=51)),
                ('dev_iosapp_img', models.ImageField(upload_to='iosapp_img/')),
                ('dev_iosapp_desc', models.TextField()),
                ('dev_iosapp_img_screen', models.ImageField(upload_to='iosapp_img/laptop_screen')),
            ],
        ),
        migrations.CreateModel(
            name='DevServiceDescIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_service_iosapp_desc', models.CharField(max_length=551)),
            ],
        ),
        migrations.CreateModel(
            name='DevServiceIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_service_iosapp_title', models.CharField(max_length=51)),
                ('dev_servic_iosapp_img', models.ImageField(upload_to='iosapp_img/dev_service')),
            ],
        ),
        migrations.CreateModel(
            name='FaqIosAPPDev',
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
            name='GetStartIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iosapp_title', models.CharField(max_length=251)),
                ('iosapp_desc', models.CharField(max_length=551)),
                ('iosapp_img1', models.ImageField(upload_to='iosapp_ico_img/')),
                ('iosapp_img_title1', models.CharField(max_length=151)),
                ('iosapp_img2', models.ImageField(upload_to='iosapp_ico_img/')),
                ('iosapp_img_title2', models.CharField(max_length=151)),
                ('iosapp_img3', models.ImageField(upload_to='iosapp_ico_img/')),
                ('iosapp_img_title3', models.CharField(max_length=151)),
                ('iosapp_img4', models.ImageField(upload_to='iosapp_ico_img/')),
                ('iosapp_img_title4', models.CharField(max_length=151)),
            ],
        ),
        migrations.CreateModel(
            name='IosAPPDevCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iosapp_dev_title', models.CharField(max_length=51)),
                ('iosapp_dev_desc', models.TextField()),
                ('iosapp_dev_img', models.ImageField(upload_to='iosapp_img/django_dev_company')),
            ],
        ),
        migrations.CreateModel(
            name='SolutionExpertiseIosAPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sol_exper_iosapp_title', models.CharField(max_length=51)),
                ('sol_exper_iosapp_img', models.ImageField(upload_to='iosapp_img/solution_expertise')),
            ],
        ),
    ]