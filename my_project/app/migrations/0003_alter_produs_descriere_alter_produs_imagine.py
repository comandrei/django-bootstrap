# Generated by Django 5.0.1 on 2024-01-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_produs_pret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produs",
            name="descriere",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="produs",
            name="imagine",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
