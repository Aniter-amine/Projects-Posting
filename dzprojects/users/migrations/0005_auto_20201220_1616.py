# Generated by Django 3.0.1 on 2020-12-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_prof_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]