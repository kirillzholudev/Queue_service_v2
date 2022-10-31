# Generated by Django 4.1.2 on 2022-10-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_remove_company_specialization_company_specialization'),
        ('guest_serv', '0004_alter_guest_options_remove_guest_name_guest_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='service',
        ),
        migrations.AddField(
            model_name='guest',
            name='service',
            field=models.ManyToManyField(to='general.specialization'),
        ),
    ]