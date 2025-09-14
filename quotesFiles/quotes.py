import random
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "In the middle of every difficulty lies opportunity.",
    "Happiness depends upon ourselves.",
    "Turn your wounds into wisdom.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It always seems impossible until it’s done.",
    "Don’t count the days, make the days count.",
    "Act as if what you do makes a difference. It does.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "What we think, we become.",
    "Believe you can and you're halfway there.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "Don’t let yesterday take up too much of today.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Dream big and dare to fail.",
    "The best way to predict the future is to create it.",
    "Doubt kills more dreams than failure ever will.",
    "Start where you are. Use what you have. Do what you can.",
]
def randomQuote():
    with open("textfiles/quotes.txt",'r') as file:
        qoutesLst =file.readlines()
    return qoutesLst[random.randint(0,20)]
