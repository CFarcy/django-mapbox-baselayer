# Generated by Django 2.2.7 on 2019-12-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapbox_baselayer', '0002_auto_20191129_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baselayertile',
            name='base_layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiles', to='mapbox_baselayer.MapBaseLayer'),
        ),
    ]
