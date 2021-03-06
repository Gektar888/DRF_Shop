# Generated by Django 4.0.2 on 2022-02-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created_date', models.DateField(auto_now=True)),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]
