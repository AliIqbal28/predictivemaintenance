# Generated by Django 3.1.2 on 2020-10-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictiveModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='engineTemp',
            field=models.FloatField(null=True),
        ),
    ]