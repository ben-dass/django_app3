# Generated by Django 4.2.16 on 2024-12-03 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_best_selling_alter_book_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_best_selling',
            new_name='is_best_seller',
        ),
    ]
