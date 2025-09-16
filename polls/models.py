from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TagCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tag category"
        verbose_name_plural = "Tag categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        TagCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tags",
    )

    def __str__(self):
        return self.name


class Quotes(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="quotes")
    tags = models.ManyToManyField(Tag, blank=True, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)  # new field
    featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)  # new field

    def __str__(self):
        author_name = self.author.name if self.author_id else "Unknown"
        return f'"{self.content}" by {author_name}'
