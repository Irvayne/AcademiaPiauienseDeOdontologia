# Generated by Django 2.0.8 on 2018-09-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estatuto',
            name='conteudo',
            field=models.CharField(max_length=1000),
        ),
    ]
