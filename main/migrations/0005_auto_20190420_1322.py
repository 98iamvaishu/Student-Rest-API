# Generated by Django 2.1 on 2019-04-20 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190419_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('organization', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='organization',
        ),
        migrations.AddField(
            model_name='signup',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='signin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
