# Generated by Django 3.1.4 on 2020-12-11 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapi', '0003_available_book_boolean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available_book',
            name='boolean',
        ),
    ]
