# Generated by Django 2.2.5 on 2019-12-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0050_dscclass3'),
    ]

    operations = [
        migrations.AddField(
            model_name='dscclass3',
            name='dsc_class3_contact',
            field=models.CharField(default='', max_length=251),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dscclass3',
            name='dsc_class3_contact_no',
            field=models.CharField(default='', max_length=251),
            preserve_default=False,
        ),
    ]
