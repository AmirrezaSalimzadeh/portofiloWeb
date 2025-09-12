import random
def randomQuote():
    address = '/home/amirreza/myblog/polls/textfiles/quotes.txt'
    with open(address,'r') as file:
        qoutesLst =file.readlines()
    return qoutesLst[random.randint(0,20)]