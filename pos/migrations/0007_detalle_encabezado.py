# Generated by Django 2.2.6 on 2019-11-04 01:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_auto_20191103_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encabezado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('precio_venta', models.FloatField()),
                ('encabezado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Encabezado')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Producto')),
            ],
        ),
    ]