# Generated by Django 4.0.2 on 2022-03-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtmalar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyurtmajadval',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
