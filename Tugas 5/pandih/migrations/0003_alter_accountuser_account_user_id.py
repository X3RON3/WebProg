# Generated by Django 5.0.6 on 2024-06-25 05:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandih', '0002_rename_pandih_acco_account_11c995_idx_pandih_acco_account_5b97e1_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('1f960fde-63c0-4f5c-8108-a69c0cad534f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
