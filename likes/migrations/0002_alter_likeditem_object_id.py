# Generated by Django 4.1.2 on 2022-12-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeditem',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]