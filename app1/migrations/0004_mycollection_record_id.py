# Generated by Django 4.1.9 on 2023-05-15 18:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycollection',
            name='record_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
