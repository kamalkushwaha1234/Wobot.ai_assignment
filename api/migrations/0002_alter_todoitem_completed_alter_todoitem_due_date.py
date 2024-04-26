# Generated by Django 5.0.4 on 2024-04-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]