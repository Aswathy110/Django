# Generated by Django 5.1.3 on 2024-11-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0004_alter_register_password_alter_register_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='userid',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]