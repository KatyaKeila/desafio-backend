# Generated by Django 4.1.5 on 2023-02-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0003_alter_form_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="file",
            field=models.FileField(upload_to="txt/"),
        ),
    ]
