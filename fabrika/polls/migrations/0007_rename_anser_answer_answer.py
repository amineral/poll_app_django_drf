# Generated by Django 3.2.5 on 2021-07-12 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210712_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='anser',
            new_name='answer',
        ),
    ]