"""
    Written by Madeline Ellingson
    10/21/2023
"""
from statistics import mean

num_of_cards = 0
num_of_items = 0
prices = []

# Take in input for the num_of_cards and num_of_items
something = input().split()
num_of_cards = int(something[0])
num_of_items = int(something[1])

max_card = 0
max_price_wines_but_column = []

prices_but_card = []
prices_but_card_but_column = []


# Now go through and get the prices for each card
for i in range(num_of_cards):
    something_else = input().split()
    card = []
    # Convert to int
    for price in something_else:
        card.append(int(price))

    prices_but_card.append(card)

# Now convert to columns?
for i in range(num_of_items):
    column = []
    for j in range(num_of_cards):
        column.append(prices_but_card[j][i])
    prices_but_card_but_column.append(column)

max_price_wine_and_card = {}

i = 0

for wine in prices_but_card_but_column:
    max_price_wine_and_card[i] = max(wine)
    i += 1

cards_and_max_price_count = {}

card_num = 1
common_max = -1

max_cards = []

for card in range(0, num_of_cards):
    if max_price_wine_and_card[card] == common_max:
        max_cards.append(card + 1)
    else:
        common_max = max_price_wine_and_card[card]

averages = {}

if(len(max_cards) == 1):
    print(max_cards[0])
else:
    # take averages
    for card in max_cards:
        averages[card] = (mean(prices_but_card[card - 1]))

    largest_avg = max(averages.values())

    for card in averages:
        if averages[card] == largest_avg:
            print(card)
            break















