# Generated by Django 3.2.12 on 2022-04-27 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='fuck_name',
            new_name='name',
        ),
    ]
