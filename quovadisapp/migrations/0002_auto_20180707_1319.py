# Generated by Django 2.0.6 on 2018-07-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quovadisapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='sub_text',
            field=models.CharField(default='Luxury Boutique Hotel', max_length=300),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text',
            field=models.CharField(default='Welcome to Quo Vadis', max_length=200),
        ),
    ]