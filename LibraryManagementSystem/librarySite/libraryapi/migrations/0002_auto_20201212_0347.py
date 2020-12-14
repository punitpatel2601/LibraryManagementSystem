# Generated by Django 3.1.4 on 2020-12-12 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryapi.series'),
        ),
        migrations.AlterField(
            model_name='person',
            name='books_withdrawn',
            field=models.IntegerField(default=0, null=True),
        ),
    ]