# Generated by Django 2.2.7 on 2019-11-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_doc',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_image1',
            field=models.ImageField(blank=True, upload_to='contract_image'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_image2',
            field=models.ImageField(blank=True, upload_to='contract_image'),
        ),
    ]
