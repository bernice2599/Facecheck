# Generated by Django 4.0.2 on 2023-02-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_attendance_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_face', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=70)),
                ('l_name', models.CharField(max_length=70)),
                ('student_number', models.CharField(max_length=200)),
                ('emaill', models.EmailField(max_length=254)),
                ('coursee', models.CharField(choices=[('BSIT', 'BSIT'), ('BSCS', 'BSCS')], default='employee', max_length=20, null=True)),
                ('present', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
