# Generated by Django 4.1.5 on 2023-02-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_name',
            new_name='author_lname',
        ),
        migrations.AddField(
            model_name='author',
            name='author_fname',
            field=models.CharField(default='Abcd', max_length=20),
        ),
    ]