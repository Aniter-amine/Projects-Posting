# Generated by Django 3.0.1 on 2020-12-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201220_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='bio',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
