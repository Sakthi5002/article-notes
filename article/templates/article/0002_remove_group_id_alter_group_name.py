# Generated by Django 4.2.16 on 2024-11-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]