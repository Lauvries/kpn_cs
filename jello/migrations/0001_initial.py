# Generated by Django 4.0.1 on 2022-01-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
                ('house_number', models.IntegerField()),
                ('house_number_suffix', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
