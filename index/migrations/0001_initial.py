# Generated by Django 2.1.3 on 2019-01-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=4)),
                ('phone_number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('booked_date', models.DateField()),
                ('booked_time', models.CharField(max_length=5)),
                ('guests_number', models.IntegerField(default=0)),
                ('customer_notes', models.TextField(blank=True, default='lorem ipsum')),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_subscribed', models.BooleanField(default=False)),
            ],
        ),
    ]
