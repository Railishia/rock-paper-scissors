import random
import choice_num_to_fig
import who_wins

print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
player_choice = int(input())
computer_choice = random.randint(0,2)

choice_num_to_fig.choice_num_to_fig(player_choice, 'user')
choice_num_to_fig.choice_num_to_fig(computer_choice,'computer')

who_wins.who_wins(player_choice, computer_choice)
