# Generated by Django 3.2.8 on 2022-05-22 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
