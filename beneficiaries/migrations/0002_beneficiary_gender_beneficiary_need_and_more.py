# Generated by Django 5.1.6 on 2025-03-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='need',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
