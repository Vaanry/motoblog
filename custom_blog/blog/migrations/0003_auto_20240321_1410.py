# Generated by Django 3.2.16 on 2024-03-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-created_at',), 'verbose_name': 'комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=20, null=True, verbose_name='Местоположение'),
        ),
    ]