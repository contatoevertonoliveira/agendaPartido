# Generated by Django 3.2.3 on 2021-05-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210524_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
