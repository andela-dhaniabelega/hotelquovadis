# Generated by Django 2.0.6 on 2018-07-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quovadisapp', '0002_auto_20180707_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='sub_text',
            field=models.TextField(default='Luxury Boutique Hotel', max_length=300),
        ),
    ]
