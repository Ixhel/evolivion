# Generated by Django 5.0.4 on 2024-04-26 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NMX_R_025_SCFI_2015', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logmessage',
            old_name='message',
            new_name='empresa',
        ),
    ]