# Generated by Django 5.0.1 on 2024-01-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_elev_elevcurs_elev_cursuri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=50)),
                ('continut', models.CharField(max_length=300)),
                ('visible_from', models.DateTimeField()),
                ('end_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]