# Generated by Django 3.2.9 on 2021-11-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
    ]
