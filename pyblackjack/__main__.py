import random
from time import sleep


def initialiseDeck(numDecks):
    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suits = ['♦️', '♠️', '♥️', '♣️']
    card_deck = []
    for x in range(numDecks):
        for suit in card_suits:
            for card in card_values:
                card_deck.append(card + ' ' + suit)
    return card_deck


def drawCard():
    # Crash Gard Against Drawing without any cards in the deck
    if len(gameState['cards']) == 0:
        print("You've run out of cards!")
        print("Game Over")
        gameState['player_turn'] = False
        gameState['cpu_turn'] = False
        return None

    # Crash Gard against drawing the last card in the deck
    if len(gameState['cards']) == 1:
        card_pnt = 0
    else:
        card_pnt = random.randint(0, len(gameState['cards']) - 1)

    card = gameState['cards'][card_pnt]
    del gameState['cards'][card_pnt]
    return card


def initGameState():
    return {
        "player_score": 0,
        "cpu_score": 0,
        "cpu_mood": 0,
        "player_turn": True,
        "cpu_turn": False,
        "cards": initialiseDeck(1)
    }


def getValue(card):
    if card == 'K':
        return 13
    if card == 'Q':
        return 12
    if card == 'J':
        return 11
    if card == 'A':
        return 1
    return int(card)


def playTurn():
    card = drawCard()

    # Safely End if no card is drawn
    if card is None:
        return None

    gameState['player_score'] += getValue(card.split()[0])
    print("You Drew: " + card)
    if gameState['player_score'] == 21:
        print(str(gameState['player_score']) + "! BlackJack! You Win!")
        gameState['player_turn'] = False
        gameState['cpu_turn'] = False
    elif gameState['player_score'] > 21:
        print(str(gameState['player_score']) + "! Bust! You Lose!")
        gameState['player_turn'] = False
        gameState['cpu_turn'] = False
    else:
        answered = False
        while not answered:
            answer = input("Your Score is: " + str(gameState['player_score']) + ".\n(S)tick or (T)wist?\n")
            if str.lower(answer) == 's':
                print("You stick with a score of " + str(gameState['player_score']) + ".")
                gameState['player_turn'] = False
                gameState['cpu_turn'] = True
                answered = True
                continue
            elif str.lower(answer) == 't':
                print("Let's draw again!")
                answered = True
                continue
            else:
                print("Huh?")
    print()
    pass


def cpuTurn():
    card = drawCard()

    # Safely End if no card is drawn
    if card is None:
        return None

    gameState['cpu_score'] += getValue(card.split()[0])
    print("The Dealer Drew: " + card)
    print("The Dealer's Score : " + str(gameState['cpu_score']))
    if gameState['cpu_score'] == 21:
        print(str(gameState['cpu_score']) + "! BlackJack! The Dealer wins...")
        gameState['cpu_turn'] = False
    elif gameState['cpu_score'] > 21:
        print(str(gameState['cpu_score']) + "! Bust! You Win!")
        gameState['cpu_turn'] = False
    else:
        print(str(gameState['cpu_score']) + "! The Dealer's gonna draw again!")
        sleep(2)
    print()
    pass


def doThing():
    pass


if __name__ == '__main__':
    running = True
    gameState = initGameState()
    random.shuffle(gameState['cards'])
    while running:
        while gameState['player_turn']:
            playTurn()
        while gameState['cpu_turn']:
            cpuTurn()
        running = False
    print("McDonalds!")
