# Generated by Django 3.1.4 on 2020-12-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='Preço',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='Tamanho',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
