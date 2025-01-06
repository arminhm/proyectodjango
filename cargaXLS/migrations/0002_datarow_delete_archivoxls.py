# Generated by Django 5.1.3 on 2024-12-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargaXLS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo_nombre', models.CharField(max_length=100)),
                ('data', models.JSONField()),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ArchivoXLS',
        ),
    ]
