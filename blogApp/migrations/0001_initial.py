# Generated by Django 2.2.1 on 2019-05-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=5)),
                ('token', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]