# Generated by Django 2.2.1 on 2019-05-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytask',
            name='states',
            field=models.CharField(choices=[('NW', 'New'), ('AC', 'Accepted'), ('CM', 'Completed'), ('D', 'Declined'), ('CN', 'Cancelled')], default='NW', max_length=9),
        ),
    ]
