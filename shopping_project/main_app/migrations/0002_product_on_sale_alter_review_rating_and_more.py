# Generated by Django 4.0.4 on 2022-05-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
