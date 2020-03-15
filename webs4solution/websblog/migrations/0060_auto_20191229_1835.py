# Generated by Django 2.2.5 on 2019-12-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0059_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=11)),
                ('last_name', models.CharField(max_length=11)),
                ('service_name', models.CharField(max_length=221)),
                ('email_id', models.CharField(max_length=21)),
                ('phone_num', models.CharField(max_length=15)),
                ('desc', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='contact_num',
            field=models.CharField(max_length=16),
        ),
    ]
