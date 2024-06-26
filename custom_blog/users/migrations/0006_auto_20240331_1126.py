# Generated by Django 3.2.16 on 2024-03-31 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motobikes', '0003_alter_motobike_options'),
        ('users', '0005_auto_20240327_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owners',
            options={'verbose_name': 'мотоцикл', 'verbose_name_plural': 'Мотоциклы'},
        ),
        migrations.RemoveField(
            model_name='motouser',
            name='moto',
        ),
        migrations.AlterField(
            model_name='motouser',
            name='motobike',
            field=models.ManyToManyField(help_text='Нет вашего мотоцикла?<br>\n        Вы можете его добавить на странице каталога.', related_name='bikes', through='users.Owners', to='motobikes.Motobike', verbose_name='Мотоцикл'),
        ),
    ]
