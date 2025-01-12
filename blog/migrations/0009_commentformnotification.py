# Generated by Django 4.0.1 on 2022-02-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_category_id_alter_comment_id_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentFormNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('message', models.TextField()),
                ('from_mail', models.EmailField(max_length=50, verbose_name='From Mail')),
                ('to_mail', models.EmailField(max_length=50, verbose_name='To Mail')),
            ],
        ),
    ]
