# Generated by Django 3.1 on 2020-10-24 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='branch_id',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
