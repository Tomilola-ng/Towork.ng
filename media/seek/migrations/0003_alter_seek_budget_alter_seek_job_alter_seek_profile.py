# Generated by Django 4.1.2 on 2022-12-29 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
        ('users', '0001_initial'),
        ('seek', '0002_alter_seek_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seek',
            name='budget',
            field=models.PositiveIntegerField(verbose_name='Your Budget in Naira'),
        ),
        migrations.AlterField(
            model_name='seek',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.job', verbose_name='Select a service'),
        ),
        migrations.AlterField(
            model_name='seek',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeks', to='users.profile'),
        ),
    ]
