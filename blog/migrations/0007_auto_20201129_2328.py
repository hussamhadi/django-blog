# Generated by Django 3.1.3 on 2020-11-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201129_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_publish',
            new_name='publish',
        ),
    ]
