# Generated by Django 2.0.7 on 2018-08-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupAndLogin', '0007_auto_20180806_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Item',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]