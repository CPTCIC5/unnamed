# Generated by Django 5.1.1 on 2024-10-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='industry_type',
            field=models.IntegerField(choices=[(1, 'Trading'), (2, 'Manufacturing'), (3, 'Service'), (4, 'Others')]),
        ),
    ]