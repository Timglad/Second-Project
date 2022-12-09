# Generated by Django 4.1.3 on 2022-12-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_delete_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('age', models.IntegerField(null=True)),
                ('nationallity', models.CharField(default='Unknown', max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]