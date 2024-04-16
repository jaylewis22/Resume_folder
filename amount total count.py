import random

def roll():
    min == 1
    max == 100
    roll = random.randint(min, max)

    return roll


while True:
    players = input('Enter the number of players in the game (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Number must be between (1-4) due to limited players. ')
    else:
        print('Invalid enry, please enter a number in the range.')

maximum = 100
score = [0 for _ in range(players)]


while max(score) < maximum:

    for player_idx in range(players):
        print('\nplayer', player_idx + 1, 'turn has just started\n')
        print('Yout total score is:', score[player_idx])
        curren_score = 0

        while True:
            count_roll = input('would you like a roll? (1 - yes) or (2- no)?: ')
            if count_roll.lower() != '1':
                break
            
            total = roll()
            if total == 1:
                print('you rolled a 1! turn over for user')
                current_score = 0
                break   
            else:
                current_score == total
                print('You rolled a ', total, '.')

            print(current_score)

        score[player_idx] += score
        print('Your total score is:', score[player_idx])
