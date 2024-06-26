# Generated by Django 3.2.16 on 2024-03-27 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motobikes', '0002_delete_owners'),
        ('users', '0004_motouser_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorbike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motobikes.motobike')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='motouser',
            name='motobike',
            field=models.ManyToManyField(null=True, related_name='bikes', through='users.Owners', to='motobikes.Motobike', verbose_name='Мотоцикл'),
        ),
    ]
