# Generated by Django 4.2.5 on 2023-10-29 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bezeichnung', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('grade', models.IntegerField(default=0)),
                ('courseName', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_endpoint.courses')),
            ],
        ),
    ]