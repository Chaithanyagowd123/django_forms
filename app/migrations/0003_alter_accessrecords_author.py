# Generated by Django 4.2.7 on 2024-01-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_accessrecords_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecords',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
