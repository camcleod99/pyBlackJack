import random


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
        gameState['game_over'] = True
        return None

    # Crash Gard against drawing the last card in the deck
    if len(gameState['cards']) == 1:
        card_pnt = 0
    else:
        card_pnt = random.randint(0, len(gameState['cards']) - 1)

    # print("Cards Left: " + str(len(gameState['cards'])))
    # print("Index of Card Drawn: "+str(card_pnt))
    card = gameState['cards'][card_pnt]
    del gameState['cards'][card_pnt]
    return card


def initGameState():
    return {
        "player_score": 0,
        "dealer_score": 0,
        "dealer_mood": 0,
        "game_over": False,
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
    print("You Drew: "+card)
    print("Your Score : "+str(gameState['player_score']))
    if gameState['player_score'] == 21:
        print("BlackJack! You Win!")
        gameState['game_over'] = True
    if gameState['player_score'] > 21:
        print("Bust! You Lose...")
        gameState['game_over'] = True
    print()
    pass


if __name__ == '__main__':
    gameState = initGameState()
    random.shuffle(gameState['cards'])
    while not gameState['game_over']:
        playTurn()
    print("McDonalds!")
