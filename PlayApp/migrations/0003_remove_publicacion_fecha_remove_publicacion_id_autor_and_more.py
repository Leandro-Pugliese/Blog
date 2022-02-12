# Generated by Django 4.0.1 on 2022-01-30 11:37

import PlayApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0002_rename_nombre_de_usuario_usuario_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='id_autor',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha actualización'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fecha_publi',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha publicación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='', upload_to=PlayApp.models.upload_publicacion),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
