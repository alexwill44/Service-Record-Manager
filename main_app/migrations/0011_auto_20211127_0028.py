# Generated by Django 3.1.2 on 2021-11-27 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20211127_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='part',
        ),
        migrations.AddField(
            model_name='part',
            name='part',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='part', to='main_app.record'),
        ),
    ]
