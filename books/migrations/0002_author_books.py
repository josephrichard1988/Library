# Generated by Django 4.1.5 on 2023-02-11 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='author_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='author.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
        ),
    ]
