# Generated by Django 2.0.7 on 2018-07-22 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20180722_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]
