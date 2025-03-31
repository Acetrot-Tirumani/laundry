# Generated by Django 4.2.7 on 2025-03-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='launderer',
            name='max_orders_per_day',
            field=models.PositiveIntegerField(default=20, help_text='Maximum number of orders this launderer can handle per day'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_slot',
            field=models.CharField(blank=True, choices=[('morning', 'Morning (8 AM - 12 PM)'), ('afternoon', 'Afternoon (12 PM - 4 PM)'), ('evening', 'Evening (4 PM - 8 PM)')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='estimated_completion_time',
            field=models.DateTimeField(blank=True, help_text='Estimated time when the order will be completed', null=True),
        ),
    ]
