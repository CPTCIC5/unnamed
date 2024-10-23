# Generated by Django 5.1.1 on 2024-10-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0003_entity_currency_type_entity_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='state',
            field=models.IntegerField(choices=[(1, 'Andhra Pradesh'), (2, 'Arunachal Pradesh '), (3, 'Assam'), (4, 'Bihar'), (5, 'Chhattisgarh'), (6, 'Goa'), (7, 'Gujarat'), (8, 'Haryana'), (9, 'Himachal Pradesh'), (10, 'Jammu and Kashmir '), (11, 'Jharkhand'), (12, 'Karnataka'), (13, 'Kerala'), (14, 'Madhya Pradesh'), (15, 'Maharashtra'), (16, 'Manipur'), (17, 'Meghalaya'), (18, 'Mizoram'), (19, 'Nagaland'), (20, 'Odisha'), (21, 'Punjab'), (22, 'Rajasthan'), (23, 'Sikkim'), (24, 'Tamil Nadu'), (25, 'Telangana'), (26, 'Tripura'), (27, 'Uttar Pradesh'), (28, 'Uttarakhand'), (29, 'West Bengal'), (30, 'Andaman and Nicobar Islands'), (31, 'Chandigarh'), (32, 'Dadra and Nagar Haveli'), (32, 'Daman and Diu'), (33, 'Lakshadweep'), (34, 'Delhi'), (35, 'Puducherry')]),
        ),
    ]
