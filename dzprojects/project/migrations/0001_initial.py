# Generated by Django 3.0.1 on 2020-12-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.CharField(max_length=256)),
                ('author_id', models.CharField(max_length=256)),
                ('author_avatar', models.CharField(max_length=256)),
                ('website_link', models.CharField(blank=True, max_length=500, null=True)),
                ('repository_link', models.CharField(blank=True, max_length=500, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('project_views', models.IntegerField(default=0)),
            ],
        ),
    ]