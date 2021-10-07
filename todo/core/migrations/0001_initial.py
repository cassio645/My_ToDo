# Generated by Django 3.2.8 on 2021-10-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('done', models.BooleanField(default=False, verbose_name='Finalizada')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
            ],
        ),
    ]
