# Generated by Django 4.1.2 on 2022-10-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
