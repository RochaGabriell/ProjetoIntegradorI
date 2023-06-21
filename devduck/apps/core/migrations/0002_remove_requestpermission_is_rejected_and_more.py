# Generated by Django 4.2.1 on 2023-06-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestpermission',
            name='is_rejected',
        ),
        migrations.AlterField(
            model_name='requestpermission',
            name='is_approved',
            field=models.BooleanField(blank=True, null=True, verbose_name='Aprovado'),
        ),
    ]