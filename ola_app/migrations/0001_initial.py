# Generated by Django 2.0.4 on 2018-04-27 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=20)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('mobile_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='booked_to',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ola_app.Rider'),
        ),
    ]
