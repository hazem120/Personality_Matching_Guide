# Generated by Django 3.1.1 on 2020-09-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0005_auto_20200919_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]