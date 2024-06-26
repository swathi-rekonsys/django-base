# Generated by Django 5.0.3 on 2024-03-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SwathiDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=100)),
                ('login_id', models.CharField(max_length=100)),
                ('desg', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('company', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
