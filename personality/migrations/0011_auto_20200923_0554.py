# Generated by Django 3.1.1 on 2020-09-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0010_personality_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personality',
            name='slug',
        ),
        migrations.AddField(
            model_name='personality',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='اسمك او لقبك الذي سيظهر في البحث'),
        ),
    ]
