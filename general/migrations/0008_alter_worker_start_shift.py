# Generated by Django 4.1.2 on 2022-10-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='start_shift',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
