# Generated by Django 4.2.1 on 2023-05-19 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'productor',
                'verbose_name_plural': 'productores',
            },
        ),
    ]
