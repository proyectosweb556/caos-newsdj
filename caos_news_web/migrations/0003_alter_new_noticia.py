# Generated by Django 3.2 on 2021-06-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caos_news_web', '0002_auto_20210629_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='noticia',
            field=models.TextField(default='email'),
        ),
    ]
