# Generated by Django 4.1.5 on 2023-01-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='floor',
            field=models.IntegerField(max_length=20),
        ),
    ]