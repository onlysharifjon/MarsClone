# Generated by Django 5.0.2 on 2024-03-09 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('directory', models.CharField(choices=[('Fronted', 'Fronted'), ('Backend', 'Backend'), ('Design', 'Design'), ('Starter', 'Starter')], max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='password',
            field=models.BigIntegerField(default=4321),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('coins', models.IntegerField()),
                ('students', models.ManyToManyField(to='Users.studentmodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.teachers')),
            ],
        ),
    ]
