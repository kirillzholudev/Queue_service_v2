# Generated by Django 4.1.2 on 2022-10-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_alter_company_options'),
        ('guest_serv', '0002_guest_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='service',
            field=models.ManyToManyField(to='general.specialization'),
        ),
    ]
