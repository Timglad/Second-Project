# Generated by Django 4.1.3 on 2022-12-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='path./placehlder.png', upload_to=''),
        ),
    ]
