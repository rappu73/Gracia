# Generated by Django 4.2 on 2023-04-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_complex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вид массажа')),
                ('price1', models.CharField(max_length=50, verbose_name='Цена за 1 сеанс')),
                ('price5', models.CharField(max_length=50, verbose_name='Цена за 5 сеансов')),
                ('price10', models.CharField(max_length=50, verbose_name='Цена за 10 сеансов')),
            ],
        ),
    ]
