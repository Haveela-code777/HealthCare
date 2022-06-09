# Generated by Django 3.1.4 on 2022-06-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeartDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('cp', models.IntegerField(blank=True, null=True)),
                ('trestbps', models.IntegerField(blank=True, null=True)),
                ('chol', models.IntegerField(blank=True, null=True)),
                ('fbs', models.IntegerField(blank=True, null=True)),
                ('restecg', models.IntegerField(blank=True, null=True)),
                ('thalach', models.IntegerField(blank=True, null=True)),
                ('exang', models.IntegerField(blank=True, null=True)),
                ('oldpeak', models.IntegerField(blank=True, null=True)),
                ('slope', models.IntegerField(blank=True, null=True)),
                ('ca', models.IntegerField(blank=True, null=True)),
                ('thal', models.IntegerField(blank=True, null=True)),
                ('target', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
