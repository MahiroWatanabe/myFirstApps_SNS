# Generated by Django 4.1.2 on 2023-03-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "投稿", "verbose_name_plural": "投稿一覧"},
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
