# Generated by Django 5.1.3 on 2024-12-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communities',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]