# Generated by Django 2.0.7 on 2019-06-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0004_auto_20190605_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycinfo',
            name='address',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
