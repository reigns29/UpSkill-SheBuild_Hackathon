# Generated by Django 4.1.5 on 2023-01-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]