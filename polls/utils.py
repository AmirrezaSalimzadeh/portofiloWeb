import random

from .models import Quotes


def randomQuote():
    quotes = list(
        Quotes.objects.select_related("author").prefetch_related("tags__category")
    )
    if not quotes:
        return None
    random_quote = random.choice(quotes)
    category_name = next(
        (
            tag.category.name
            for tag in random_quote.tags.all()
            if tag.category is not None
        ),
        None,
    )
    return {"quote": random_quote, "category": category_name}
