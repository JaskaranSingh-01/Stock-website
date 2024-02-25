# Generated by Django 4.1.7 on 2023-03-27 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customauth", "0003_alter_useraccount_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useraccount",
            name="username",
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="email",
            field=models.EmailField(
                max_length=60,
                null=True,
                unique=True,
                validators=[django.core.validators.EmailValidator()],
                verbose_name="Email",
            ),
        ),
    ]
