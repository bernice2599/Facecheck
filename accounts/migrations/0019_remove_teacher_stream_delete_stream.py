# Generated by Django 4.0.2 on 2023-02-08 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_classroom_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='stream',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]
