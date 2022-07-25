# Generated by Django 4.0.4 on 2022-07-25 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_teacher', to='api.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('is_monitor', models.BooleanField(default=False)),
                ('div', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.division')),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.std')),
            ],
            options={
                'unique_together': {('roll_no', 'std', 'div')},
            },
        ),
    ]
