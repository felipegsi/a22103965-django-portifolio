# Generated by Django 4.2.2 on 2023-07-24 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0011_projeto_dificuldade_projeto_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Praia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('regiao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portifolio.regiao')),
            ],
        ),
    ]
