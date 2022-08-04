# Generated by Django 4.0.6 on 2022-08-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(db_index=True, max_length=255)),
                ('filepath', models.FilePathField()),
                ('filesize', models.IntegerField()),
                ('fileid', models.CharField(db_index=True, max_length=255)),
                ('up_path', models.CharField(db_index=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]