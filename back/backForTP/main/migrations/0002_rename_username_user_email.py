# Generated by Django 4.1.7 on 2023-03-26 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
    ]
