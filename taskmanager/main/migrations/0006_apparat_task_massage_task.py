# Generated by Django 4.2 on 2023-04-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_apparat_options_alter_complex_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apparat',
            name='task',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='massage',
            name='task',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
