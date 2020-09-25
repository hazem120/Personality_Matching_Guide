# Generated by Django 3.1.1 on 2020-09-19 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personality', '0004_person_facebooklink'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]