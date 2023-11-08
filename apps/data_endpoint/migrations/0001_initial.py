# Generated by Django 4.2.5 on 2023-11-08 14:04

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
                ('name', models.CharField(default=None, max_length=200)),
                ('grade_first', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True)),
                ('grade_second', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True)),
                ('semester', models.CharField(default=None, max_length=200, null=True)),
                ('sum_of_credits', models.CharField(default=None, max_length=200, null=True)),
                ('partial_credits', models.CharField(default=None, max_length=200, null=True)),
                ('course_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data_endpoint.courses')),
            ],
        ),
    ]
