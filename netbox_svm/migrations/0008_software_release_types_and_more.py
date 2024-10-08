# Generated by Django 4.2.9 on 2024-02-07 21:01

from django.db import migrations, models
import netbox_svm.models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_svm', '0007_softwareproductinstallation_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarelicense',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='softwarelicense',
            name='license_amount',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='softwarelicense',
            name='support',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='softwareproduct',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='softwareproductinstallation',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='documentation_url',
            field=netbox_svm.models.LaxURLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='end_of_support',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='file_checksum',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='file_link',
            field=netbox_svm.models.LaxURLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='filename',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='softwareproductversion',
            name='release_type',
            field=models.CharField(default='S', max_length=3),
        ),
    ]
