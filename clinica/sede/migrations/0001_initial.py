# Generated by Django 4.1.2 on 2022-11-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cod', models.IntegerField()),
                ('tel', models.IntegerField()),
                ('dir', models.CharField(max_length=40)),
            ],
        ),
    ]
