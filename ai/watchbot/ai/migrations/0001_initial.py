# Generated by Django 4.0.3 on 2022-04-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Premise',
            fields=[
                ('ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Name', models.TextField()),
            ],
            options={
                'db_table': 'Premise',
            },
        ),
    ]
