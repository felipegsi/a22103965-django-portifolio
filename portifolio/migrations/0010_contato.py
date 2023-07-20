# Generated by Django 4.2.2 on 2023-07-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0009_artigo_conteudo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('assunto', models.CharField(choices=[('duvida', 'Dúvida'), ('sugestao', 'Sugestão'), ('reclamacao', 'Reclamação'), ('outro', 'Outro')], max_length=20)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
