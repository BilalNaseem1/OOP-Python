import random
import json

SUIT_TUPLE = (
    'Spades',
    'Hearts',
    'Clubs',
    'Diamonds'
)

RANK_TUPLE = (
    'Ace',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King'
)

# The game randomly selects 8 cards from a standard deck of 52 cards.
N_Cards = 8

# Takes a list of cards (deckListIn) as input.
# Removes and returns the last card from the list using .pop().
def getCard(cardList):
    thisCard = cardList.pop()
    return thisCard


# Takes a list of cards (deckListIn) as input.
# Makes a copy of the input deck so the original stays unchanged.
# Uses random.shuffle() to shuffle the copy in place.
def shuffle(cardList):
    shuffledList = cardList.copy()
    random.shuffle(shuffledList)
    return shuffledList

startingDeckList = []
for suit in SUIT_TUPLE:
    for i, card in enumerate(RANK_TUPLE):
        cardDict = {
            'rank': card,
            'suit': suit,
            'value': i+1
        }
        startingDeckList.append(cardDict)

with open('startingDeck.json', 'w') as f:
    json.dump(startingDeckList, f, indent=4)
    

# while True:
shuffled_deck = shuffle(startingDeckList)
# pick 8 cards
final_deck = []
for i in range(0, N_Cards):
    final_deck.append(shuffled_deck[i])


with open('finalDeck.json', 'w') as f:
    json.dump(final_deck, f, indent=4)


# showing the first card

while True:
    score = 50
    print("\nWelcome to Higher or Lower!")
    print("You start with 50 points.")
    print("Correct guess = +20, Wrong guess = -15.")
    print("Same value counts as wrong.\n")

    shuffled_deck = shuffle(startingDeckList)
    final_deck = shuffled_deck[:N_Cards]

    current_card = final_deck.pop(0)
    print(f"The first card is:\n {current_card['rank']} of {current_card['suit']}")

    while final_deck:
        user_input = input("Will the next card be higher (h) or lower (l)? ").lower()

        if user_input not in ('h', 'l'):
            print("Please enter a valid input")
            continue

        next_card = final_deck.pop(0)
        print(f"The next card is:\n {next_card['rank']} of {next_card['suit']}")
    
        if user_input == 'h' and next_card['value'] > current_card['value']:
            print("You were right! +20 points.\n")
            score += 20
        elif user_input == 'l' and next_card['value'] < current_card['value']:
            print("You were right! +20 points.\n")
            score += 20
        else:
            print("You were wrong. -15 points.\n")
            score -= 15

        current_card = next_card
        print(f"Current Score: {score}")

    print(f"\nGame over! Final Score: {score}")
    
        
    break
