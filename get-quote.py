from random import choice

def main():
    with open('quotes.txt') as file:
        quotes = file.readlines()
        random_quote = choice(quotes)
        print(random_quote)
