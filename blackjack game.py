import random
playerIn = True
dealerIn = True
# Deck of cards / player dealer hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'A','J','Q', 'K','A','J','Q', 'K','A','J','Q', 'K','A','J','Q', 'K']
playerHand = []
dealerHand = []

# Deal the cards
def dealCard(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)
        
# calculate the total of each hand
    
def total(hand):
    total = 0
    face = 0
    for face in hand:
        if face in range(11):
            total += face
        elif face in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            face += 1
    while face and total > 21:
        total -= 10
        face -= 1
    return total

# check for winner

def revealDealerHand():
    if len(dealerHand) ==2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
def revealPlayerHand():
    if len(playerHand) ==2:
        return playerHand[0]
    elif len(playerHand) > 2:
        return playerHand[0], playerHand[1]
# game loop

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)
print(f'dealer hand shows: {dealerHand}')
print(f'player hand shows: {playerHand}')


while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()}: ")
    print(f'You have {playerHand} for a total of {total(playerHand)}')
    if playerIn:
          stayOrhit = input('1: Stay\n2: Hit\nEnter in your choice:')
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrhit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break


if total(playerHand) == 21:
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('Blackjack! You win!')
elif total(dealerHand) == 21:
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('Blackjack! Dealer wins!')
elif total(playerHand) > 21:
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('you Bust! Dealer wins!')
elif total(dealerHand) > 21:
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('Dealer Busts! you win!')
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('Dealer wins!')
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f'\n You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print('You win!')










    
