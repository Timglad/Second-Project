# Generated by Django 4.1.3 on 2022-12-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_age_alter_userprofile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/placehlder.png', null=True, upload_to=''),
        ),
    ]
