# Generated by Django 4.2.2 on 2023-06-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pereval", "0006_perevaladded_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users", name="email", field=models.CharField(max_length=255),
        ),
    ]
