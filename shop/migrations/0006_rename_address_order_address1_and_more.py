# Generated by Django 4.2.1 on 2023-06-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='city1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='state1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='zipcode1',
        ),
    ]
