from statistics import mean

# num_of_cards = 17
# num_of_items = 8
# prices_but_card = [
# [768592562, 80658517, 135834655, 63130656, 678748721, 400870645, 365973099, 309299056],
# [55785735, 695114644, 122914940, 737713426, 812888851, 91184743, 75531013, 455368561],
# [745010016, 850447933, 976246878, 705957296, 333429982, 656970725, 530022083, 548038943],
# [649286529, 583468339, 940914825, 978546802, 78003653, 537591070, 776732611, 747102879],
# [630578674, 419356778, 279710456, 521015895, 107439298, 45843066, 505344438, 499659327],
# [603507660, 649552779, 550365415, 922060433, 496317326, 665676714, 518258593, 318421278],
# [561296860, 681098977, 914143864, 571709766, 880708450, 913356293, 230293459, 608967024],
# [236437595, 881290520, 583939123, 154226826, 614788012, 838110455, 455382451, 71101659],
# [978748061, 273784116, 65212058, 82308568, 809289220, 569343306, 378738567, 283832647],
# [302529051, 812007914, 846340931, 321538217, 262701167, 292522171, 873300483, 789686742],
# [630207942, 219279368, 337455188, 614838328, 122868381, 377120475, 807525733, 816613047],
# [768142670, 5193838, 716604462, 20703082, 551704576, 3217613, 635915377, 643315125],
# [49568620, 118186606, 160415198, 905362546, 961576576, 17383422, 345386016, 710199082],
# [856643567, 712448108, 630795339, 778205884, 394397748, 903010796, 555132643, 178269036],
# [686005982, 638243499, 83436537, 806287543, 340792693, 839338326, 130110689, 662591591],
# [624657804, 102334818, 622514062, 734948202, 497738238, 481320058, 341702638, 194357085],
# [227208193, 612892252, 845915410, 650436179, 288112426, 857903034, 486610979, 815150560]]

# Take in input for the num_of_cards and num_of_items
something = input().split()
num_of_cards = int(something[0])
num_of_items = int(something[1])

prices_but_card = []

# # Now go through and get the prices for each card
for i in range(num_of_cards):
    something_else = input().split()
    card = []
    # Convert to int
    for price in something_else:
        card.append(int(price))

    prices_but_card.append(card)

wine_prices = []

# Get all the prices for each wine
for i in range(num_of_items):
    column = []
    for j in range(num_of_cards):
        column.append(prices_but_card[j][i])
    wine_prices.append(column)

# Put the maximum wine prices in a list
maximum_wine_price_by_wine = []

for wine in wine_prices:
    maximum_wine_price_by_wine.append(max(wine))

# Count how may cards have the maximum wine prices and add that to their count
max_wine_counts = {}

for card_num in range(num_of_cards):
    max_wine_counts[card_num] = 0

    for i in range(num_of_items):
        if prices_but_card[card_num][i] == maximum_wine_price_by_wine[i]:
            max_wine_counts[card_num] += 1

# now get the largest count and add them to a list of cards
max_cards = []

max_count = max(max_wine_counts.values())

for card in max_wine_counts:
    if max_wine_counts[card] == max_count:
        max_cards.append(card)

# If there is only one card then print it
if len(max_cards) == 1:
    print(max_cards[0] + 1)
else:
    # get the average
    averages = {}
    # take averages
    for card in max_cards:
        averages[card] = (mean(prices_but_card[card]))

    largest_avg = max(averages.values())

    for card in averages:
        if averages[card] == largest_avg:
            print(card + 1)
            break

