# Generated by Django 5.0.1 on 2024-02-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_intrebare_text_raspuns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='stoc',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
