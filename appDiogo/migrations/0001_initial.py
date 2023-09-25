# Generated by Django 3.2.13 on 2023-09-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PratosMassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('tipoMassa', models.CharField(max_length=20)),
                ('dificuldade', models.CharField(choices=[('F', 'Facil'), ('M', 'Medio'), ('D', 'Dificil')], max_length=10)),
                ('numCalorias', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Utensilios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=8)),
                ('cortante', models.BooleanField()),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande')], max_length=1)),
            ],
        ),
    ]