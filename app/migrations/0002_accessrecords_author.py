# Generated by Django 4.2.7 on 2024-01-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecords',
            name='author',
            field=models.CharField(default='no author name', max_length=100),
        ),
    ]