# Generated by Django 5.0.6 on 2024-06-14 08:23

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('account_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_user_fullname', models.CharField(editable=False, max_length=255)),
                ('account_user_student_number', models.CharField(max_length=20)),
                ('account_user_created_by', models.CharField(max_length=255)),
                ('account_user_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_user_updated_by', models.CharField(max_length=255, null=True)),
                ('account_user_updated_date', models.DateTimeField(auto_now_add=True)),
                ('account_user_related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('account_user_related_user',),
                'indexes': [models.Index(fields=['account_user_id', 'account_user_related_user'], name='pandih_acco_account_11c995_idx')],
            },
        ),
    ]
