# Generated by Django 4.2.6 on 2023-10-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotinhas', '0002_rename_gotinha_gotinhas'),
    ]

    operations = [
        migrations.AddField(
            model_name='gotinhas',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]