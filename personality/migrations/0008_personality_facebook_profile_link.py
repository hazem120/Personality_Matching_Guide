# Generated by Django 3.1.1 on 2020-09-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0007_remove_personality_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='facebook_profile_link',
            field=models.CharField(max_length=500, null=True, verbose_name=' لينك بروفايل الفيسبوك '),
        ),
    ]
