# Generated by Django 2.2.6 on 2019-11-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, default='bruh', max_length=100),
            preserve_default=False,
        ),
    ]
