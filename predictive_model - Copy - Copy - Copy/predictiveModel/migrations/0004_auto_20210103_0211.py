# Generated by Django 3.1.2 on 2021-01-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictiveModel', '0003_auto_20201031_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='UUID',
            field=models.CharField(max_length=10),
        ),
    ]