# Generated by Django 5.0.4 on 2025-01-01 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titele',
            new_name='title',
        ),
    ]
