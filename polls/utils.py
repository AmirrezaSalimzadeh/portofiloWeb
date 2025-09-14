import random
from .models import Quotes
def randomQuote():
    quotes = list(Quotes.objects.all())
    if quotes:
        random_quote = random.choice(quotes)
        return random_quote.author,random_quote.content