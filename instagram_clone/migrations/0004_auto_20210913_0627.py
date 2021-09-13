# Generated by Django 3.2.7 on 2021-09-13 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram_clone', '0003_auto_20210912_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(blank=True, default='great', on_delete=django.db.models.deletion.CASCADE, to='instagram_clone.comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='instagram_clone.like'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, default='Robert', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
