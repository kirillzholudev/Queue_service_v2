# Generated by Django 4.1.2 on 2022-10-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_serv', '0004_alter_guest_options_remove_guest_name_guest_phone_and_more'),
        ('worker_ser', '0002_alter_worker_options_remove_worker_specialization'),
        ('general', '0003_alter_company_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.RemoveField(
            model_name='company',
            name='adress',
        ),
        migrations.AddField(
            model_name='company',
            name='adres',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='specialization',
            field=models.CharField(choices=[('Cash management', 'Cash management'), ('Currency exchange', 'Currency exchange'), ('New account', 'New account'), ('Deposit', 'Deposit'), ('Loan', 'Loan')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]
