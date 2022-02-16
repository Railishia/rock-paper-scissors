def who_wins(user, computer):
  
  if user == computer:
    print('Draw')
  elif user == 0:
    if computer == 1:
      print('computer wins')
    elif computer == 2:
      print('user wins')
  elif user == 1:
    if computer == 0:
      print('user wins')
    elif computer == 2:
      print('computer wins')
  elif user == 2:
    if computer == 0:
      print('computer wins')
    elif computer == 1:
      print('user wins')
