# Generated by Django 5.1.3 on 2024-12-03 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacion', '0004_category_color_item_delete_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_colors',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
