# Generated by Django 5.0.6 on 2024-06-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_app', '0003_person_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
    ]