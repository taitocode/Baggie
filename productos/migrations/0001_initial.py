# Generated by Django 2.2.6 on 2020-03-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=15)),
                ('Nombre', models.CharField(max_length=25)),
                ('Procedencia', models.CharField(max_length=30)),
                ('Variedad', models.CharField(max_length=15)),
                ('Zafra', models.CharField(max_length=15)),
            ],
        ),
    ]