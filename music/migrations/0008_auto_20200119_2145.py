# Generated by Django 3.0.2 on 2020-01-19 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200119_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='music_album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Albums'),
        ),
    ]
