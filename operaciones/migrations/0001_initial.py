# Generated by Django 2.2.6 on 2020-03-14 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empaques', '0001_initial'),
        ('usuarios', '0003_auto_20200314_1420'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Descripcion', models.CharField(max_length=25)),
                ('ID_Empaque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empaques.Empaque')),
                ('ID_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
                ('ID_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]
