# Generated by Django 4.1.7 on 2023-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_alter_user_activation_code_alter_user_audience_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_code",
            field=models.CharField(default="hbDQ0R0y75", max_length=10),
        ),
    ]