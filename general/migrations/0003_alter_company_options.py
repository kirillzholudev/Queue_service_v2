# Generated by Django 4.1.2 on 2022-10-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_alter_order_options_alter_specialization_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['pk']},
        ),
    ]
