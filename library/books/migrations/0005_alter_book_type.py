# Generated by Django 4.1.3 on 2022-12-03 17:52

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_loan_returndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.SmallIntegerField(choices=[(10, 'Ten Days Loan'), (5, 'Five Days Loan'), (2, 'Two Days Loan')], default=books.models.BookType['two_days']),
        ),
    ]