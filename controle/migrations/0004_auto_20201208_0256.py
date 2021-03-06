# Generated by Django 3.1.4 on 2020-12-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_auto_20201208_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='Preço_unitário',
            field=models.DecimalField(decimal_places=4, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Quantidade',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Total',
            field=models.DecimalField(decimal_places=4, max_digits=8, null=True),
        ),
    ]
