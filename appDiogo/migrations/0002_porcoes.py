# Generated by Django 3.2.13 on 2023-09-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDiogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porcoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]