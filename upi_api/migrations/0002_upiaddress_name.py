# Generated by Django 4.2.3 on 2023-07-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upi_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="upiaddress",
            name="name",
            field=models.CharField(default="samarth", max_length=250),
            preserve_default=False,
        ),
    ]
