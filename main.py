from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bider_list = {}
condition = True
while condition:
    bider = input("what is your name ")
    bidding_amount = int(input('What\'s your bid?: $'))
    other_player = input("Are there any other bidders? Type \'yes\' or \'no\'.").lower()
    bider_list[f"{bider}"] = bidding_amount
    if other_player == 'yes':
        clear()
    else:
        condition = False

# Get index of smallest value
values = bider_list.values()
maxvalue = max(list(values))
maxIndex = list(values).index(max(values))

# Get the corresponding key
keys = bider_list.keys()
maxkey  = list(keys)[maxIndex]

print(f'The winner is {maxkey} with a bid of ${maxvalue}')