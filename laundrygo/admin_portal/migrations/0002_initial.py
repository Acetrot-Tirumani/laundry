# Generated by Django 4.2.7 on 2025-03-23 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laundererverification',
            name='launderer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verification', to='customer.launderer'),
        ),
        migrations.AddField(
            model_name='laundererverification',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adminsupportresponse',
            name='responded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support_responses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adminsupportresponse',
            name='support_query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_responses', to='customer.customersupport'),
        ),
    ]
