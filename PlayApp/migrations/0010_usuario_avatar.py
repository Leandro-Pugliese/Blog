# Generated by Django 4.0.1 on 2022-02-12 18:45

import PlayApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0009_alter_usuario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(default='', upload_to=PlayApp.models.upload_avatar),
            preserve_default=False,
        ),
    ]
