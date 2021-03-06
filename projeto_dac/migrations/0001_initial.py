# Generated by Django 3.1.4 on 2020-12-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_edicao', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('cidade', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('area_concentracao', models.CharField(max_length=100)),
                ('instituicao_org', models.CharField(max_length=100)),
            ],
        ),
    ]
