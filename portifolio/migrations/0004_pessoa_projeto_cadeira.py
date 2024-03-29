# Generated by Django 4.2.2 on 2023-06-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0003_autor_categoria_artigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('link_linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_conclusao', models.DateField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projetos/')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano_letivo_frequentado', models.PositiveIntegerField()),
                ('semestre', models.CharField(choices=[('1', '1º semestre'), ('2', '2º semestre'), ('3', '3º semestre'), ('4', '4º semestre'), ('5', '5º semestre'), ('6', '6º semestre')], max_length=1)),
                ('creditos_ects', models.PositiveIntegerField()),
                ('topicos_abordados', models.TextField()),
                ('ranking', models.PositiveIntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')])),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='cadeiras/')),
                ('nota', models.PositiveIntegerField()),
                ('departamento', models.CharField(max_length=100)),
                ('carga_horaria', models.PositiveIntegerField()),
                ('descricao_cadeira', models.TextField()),
                ('professores', models.ManyToManyField(to='portifolio.pessoa')),
                ('projetos_realizados', models.ManyToManyField(to='portifolio.projeto')),
            ],
        ),
    ]
