# Generated by Django 4.2.1 on 2023-06-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]