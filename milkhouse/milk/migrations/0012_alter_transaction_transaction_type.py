# Generated by Django 4.0.1 on 2024-11-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0011_alter_transaction_buyer_alter_transaction_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=15),
        ),
    ]
