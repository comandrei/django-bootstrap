# Generated by Django 5.0.1 on 2024-01-25 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_recenzie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=30)),
                ('an', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ElevCurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(default=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('curs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curs')),
                ('elev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.elev')),
            ],
        ),
        migrations.AddField(
            model_name='elev',
            name='cursuri',
            field=models.ManyToManyField(through='app.ElevCurs', to='app.curs'),
        ),
    ]