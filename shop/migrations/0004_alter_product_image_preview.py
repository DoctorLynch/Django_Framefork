# Generated by Django 4.2.6 on 2023-10-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_blogs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
