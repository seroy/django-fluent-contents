# Generated by Django 1.9 on 2015-12-29 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("fluent_contents", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
            ],
            options={"verbose_name": "Article", "verbose_name_plural": "Articles"},
        ),
        migrations.CreateModel(
            name="ArticleTextItem",
            fields=[
                (
                    "contentitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="fluent_contents.ContentItem",
                    ),
                ),
                ("text", models.TextField(verbose_name="Text")),
            ],
            options={
                "db_table": "contentitem_article_articletextitem",
                "verbose_name": "Article text item",
                "verbose_name_plural": "Article text items",
            },
            bases=("fluent_contents.contentitem",),
        ),
    ]
