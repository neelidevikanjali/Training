# Generated by Django 4.0.5 on 2022-08-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='barimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
