# Generated by Django 4.0.3 on 2022-03-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
