# Generated by Django 3.1 on 2020-10-24 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_booktransaction_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktransaction',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='booktransaction',
            old_name='cooperator_id',
            new_name='cooperator',
        ),
    ]
