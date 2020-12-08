# Generated by Django 3.1.4 on 2020-12-08 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20201208_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='Preço',
            new_name='Código',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='Tamanho',
        ),
        migrations.AddField(
            model_name='produto',
            name='Preço_unitário',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='Total',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]