# Generated by Django 4.0.1 on 2022-02-09 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0007_alter_publicacion_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='publicacion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='PlayApp.publicacion'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
