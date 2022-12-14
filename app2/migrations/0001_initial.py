# Generated by Django 4.1.1 on 2022-09-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intervyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=200)),
                ('sana', models.DateField()),
                ('link', models.CharField(max_length=200)),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=300)),
                ('sana', models.DateField()),
                ('matn', models.CharField(max_length=600)),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
    ]
