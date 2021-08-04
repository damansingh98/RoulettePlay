####################################################################################################
# Name: Damandeep Singh
# Course: CS 320
# Summer 2021
####################################################################################################

import random


# user input:
print("\nWelcome to the Roulette!")
print()
print("Please pick a roulette table of your choice:")
print("American       European\n")
game_style = str(input("Type Here: "))
print()
print("Please enter your minimum and maximum bets: ")
min_bet = int(input("Min. bet ($): "))
max_bet = int(input("Max. bet ($): "))
print()
rounds = int(input("How many rounds would you like?\n"))


# spins wheel
def spinWheel():
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if game_style.lower() == 'american':
        spin = random.randint(-1, 36)  # -1 --> 00
        if spin in black:
            return True
        else:  # Red or Green
            return False

    elif game_style.lower() == "european":  # European
        spin = random.randint(0, 36)
        if spin in black:
            return True
        else:  # Red or Green
            return False
    else:
        print("Invalid input")

# variables
wins, lost, next_bet = 0, 0, 0
accum_gain, accum_loss = 0, 0
pay_out, loss = [max_bet] * rounds, [max_bet] * rounds
old_bet = min_bet
#runs the roulette game
for i in range(rounds):
    if i == rounds-1:
        continue
    elif min_bet <= max_bet:
        if spinWheel():
            wins += 1
            accum_gain += min_bet
            pay_out[i] += min_bet
            curr_bet = old_bet
            loss[i] = 0

        else:
            lost += 1
            pay_out[i] = 0
            accum_loss -= min_bet
            loss[i] += accum_loss
            next_bet = -accum_loss
            min_bet = next_bet
    else:
        min_bet = old_bet


#average payout and loss calculation
avg_payout = f"{sum(pay_out)/wins:.1f}"
avg_loss = f"{sum(loss) /lost:.1f}"
net_earn = accum_gain+accum_loss

# function to print output to screen
def display_results():
    print()
    s = ""

    print(f"Configuration:{s:<5}Number of rounds:{s:^}{rounds:>8}{s:>5}Game style{s:>5}{game_style:>8}"
      f"{s:>5}Min. bet ($):{old_bet:>10}{s:>5}Max. bet ($):{max_bet:>8}")

    print(f"\nResult: {s:>11}Accum. gain: {accum_gain:>12}"
      f"{s:<5}Accum. loss: {accum_loss:>10}{s:>5}Net (+/-): {net_earn:>12} ")

    print(f"\nWinnings: {s:>9}Greatest payout: {max(pay_out):>8}"
      f"{s:>5}Avg. payout: {avg_payout:>10}"
      f"{s:>5}Win rounds: {wins:>11}")

    print(f"\nLosses: {s:>11}Greatest loss: {min(loss):>10}"
      f"{s:>5}Avg. loss: {avg_loss:>12}"
      f"{s:>5}Losing rounds: {lost:>8}")

# Outputs results to screen
display_results()