# Generated by Django 4.2.6 on 2023-11-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_verification_code_user_verify_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активность'),
        ),
    ]
