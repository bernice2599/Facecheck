# Generated by Django 4.1.2 on 2022-10-30 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_attendance_subject'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='student',
            name='current_class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
