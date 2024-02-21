# Generated by Django 5.0 on 2024-01-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('file_name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='../static/assets/')),
            ],
        ),
        migrations.DeleteModel(
            name='User_account',
        ),
        migrations.DeleteModel(
            name='User_type',
        ),
    ]