# Generated by Django 4.1 on 2022-08-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
