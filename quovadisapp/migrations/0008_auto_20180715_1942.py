# Generated by Django 2.0.6 on 2018-07-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quovadisapp', '0007_auto_20180715_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='quovadisapp.Category'),
        ),
    ]