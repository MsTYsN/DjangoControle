# Generated by Django 4.0.3 on 2022-05-07 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('solde', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mestaoui_yassine.client')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('montant', models.FloatField()),
                ('type', models.CharField(max_length=50)),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mestaoui_yassine.compte')),
            ],
        ),
    ]
