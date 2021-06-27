from random import *

def main():
  with open('quotes.txt') as file:
    for line in file:
        print(random.choice(line))
