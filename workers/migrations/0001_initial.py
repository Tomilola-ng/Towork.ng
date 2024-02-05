# Generated by Django 4.1.2 on 2022-12-29 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(default=1234567890, null=True)),
                ('account_name', models.CharField(default='', max_length=100)),
                ('bank', models.CharField(default='', help_text='Must be a Nigerian Bank', max_length=50)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.job', verbose_name='')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
