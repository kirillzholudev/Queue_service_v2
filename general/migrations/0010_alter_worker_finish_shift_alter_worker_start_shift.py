# Generated by Django 4.1.2 on 2022-10-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_alter_worker_start_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='finish_shift',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='start_shift',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
