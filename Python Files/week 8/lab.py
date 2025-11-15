def find_winner(player1 = "rock", player2 = 'rock'):

    if player1 == player2:
        return "its a tie"

    if(player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == 'paper') or (player1 == "paper" and player2 == 'rock'):
        return "player 1 wins"
    else:
        return "player 2 wins"
    

print(find_winner())


def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
    


def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    

def report_negative_odds(lyst):
    output = []

    for num in lyst:
        if is_negative(num) and is_odd(num):
            output.append(num)

    return output

print(report_negative_odds([100,-57,12,1,-36,-15]))