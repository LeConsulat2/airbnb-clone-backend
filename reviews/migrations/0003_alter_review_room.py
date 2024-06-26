# Generated by Django 5.0.3 on 2024-06-01 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_user'),
        ('rooms', '0007_alter_room_category_alter_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='rooms.room'),
        ),
    ]
