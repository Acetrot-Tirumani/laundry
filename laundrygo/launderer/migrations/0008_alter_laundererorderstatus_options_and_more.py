# Generated by Django 4.2.7 on 2025-03-28 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('launderer', '0007_alter_laundererorderstatus_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laundererorderstatus',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='laundererorderstatus',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_updates', to=settings.AUTH_USER_MODEL),
        ),
    ]
