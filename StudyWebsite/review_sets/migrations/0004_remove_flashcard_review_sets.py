# Generated by Django 5.0.4 on 2024-04-22 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_sets', '0003_flashcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='review_sets',
        ),
    ]