# Generated by Django 5.1.3 on 2024-11-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_contact_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='alternative_mobile_number',
            field=models.IntegerField(),
        ),
    ]
