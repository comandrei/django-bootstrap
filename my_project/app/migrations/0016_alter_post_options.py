# Generated by Django 5.0.1 on 2024-01-25 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_post_created_post_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated',)},
        ),
    ]
