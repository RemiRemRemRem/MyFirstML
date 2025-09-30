cards = [10, 20, 30, 40]

def card_finder(cards, target):
    i = 0
    for value in cards:
        if value == target:
            return i
        else:
            i += 1
    else: 
        return -1

def print_results(index, target):
    if card_finder != -1:
        print(f"{target} was at position {index + 1}")
    else:
        print("Could not be found")

index = card_finder(cards, 40)
print(f"Cards: {cards}")
print_results(index, 40)