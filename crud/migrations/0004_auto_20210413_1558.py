# Generated by Django 3.2 on 2021-04-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210413_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('technology', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=200)),
                ('project', models.CharField(max_length=500)),
                ('blogs', models.CharField(max_length=500)),
                ('score', models.IntegerField(max_length=30)),
                ('placed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
