# Generated by Django 5.1.3 on 2024-11-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freitascodes', '0003_certificados_arquivo_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição da Imagem'),
        ),
    ]
