# Generated by Django 5.1.3 on 2024-11-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catgory_name', models.CharField(blank=True, max_length=100, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='cat/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_surname', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_comment', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
