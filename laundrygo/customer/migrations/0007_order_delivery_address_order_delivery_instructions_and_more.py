# Generated by Django 4.2.7 on 2025-03-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_launderer_provides_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='laundry_image',
            field=models.ImageField(blank=True, null=True, upload_to='laundry_images/'),
        ),
    ]
