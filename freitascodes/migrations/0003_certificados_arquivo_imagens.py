# Generated by Django 5.1.3 on 2024-11-12 22:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freitascodes', '0002_certificados'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificados',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='certificados', verbose_name='Arquivo'),
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.TextField(verbose_name='Descrição da Imagem')),
                ('arquivo', models.ImageField(upload_to='projetos', verbose_name='Imagem')),
                ('ordem', models.IntegerField(default=5, help_text='Quanto maior, maior a prioridade na ordenação', verbose_name='Ordem da imagem')),
                ('ativo', models.BooleanField(default=True, verbose_name='Está Disponível?')),
                ('projeto', models.ForeignKey(help_text='Projeto associado', on_delete=django.db.models.deletion.CASCADE, to='freitascodes.projetos', verbose_name='Projeto')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
                'ordering': ['projeto__name', 'ordem', 'ativo'],
            },
        ),
    ]
