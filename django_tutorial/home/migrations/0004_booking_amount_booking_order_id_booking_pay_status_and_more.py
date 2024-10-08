# Generated by Django 4.2.2 on 2024-10-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='pay_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='razorpay_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
