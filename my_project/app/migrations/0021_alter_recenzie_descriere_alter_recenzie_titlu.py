# Generated by Django 5.0.1 on 2024-02-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_intrebare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recenzie',
            name='descriere',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recenzie',
            name='titlu',
            field=models.CharField(max_length=100),
        ),
    ]