from django.db import migrations, models


def forwards_create_authors(apps, schema_editor):
    Author = apps.get_model("polls", "Author")
    Quote = apps.get_model("polls", "Quotes")

    for quote in Quote.objects.all():
        author_name = getattr(quote, "author", "")
        if not author_name:
            continue
        author_obj, _ = Author.objects.get_or_create(name=author_name)
        quote.author_temp = author_obj
        quote.save(update_fields=["author_temp"])


def backwards_remove_authors(apps, schema_editor):
    Author = apps.get_model("polls", "Author")
    Quote = apps.get_model("polls", "Quotes")

    for quote in Quote.objects.all():
        author_obj = getattr(quote, "author_temp", None)
        if author_obj:
            quote.author = author_obj.name
            quote.save(update_fields=["author"])

    Author.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_quotes_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("bio", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="TagCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "Tag category",
                "verbose_name_plural": "Tag categories",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.deletion.SET_NULL,
                        related_name="tags",
                        to="polls.tagcategory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="quotes",
            name="author_temp",
            field=models.ForeignKey(
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="quotes",
                to="polls.author",
            ),
        ),
        migrations.AddField(
            model_name="quotes",
            name="tags",
            field=models.ManyToManyField(blank=True, related_name="quotes", to="polls.tag"),
        ),
        migrations.RunPython(forwards_create_authors, backwards_remove_authors),
        migrations.RemoveField(
            model_name="quotes",
            name="author",
        ),
        migrations.RenameField(
            model_name="quotes",
            old_name="author_temp",
            new_name="author",
        ),
        migrations.AlterField(
            model_name="quotes",
            name="author",
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="quotes", to="polls.author"),
        ),
    ]
