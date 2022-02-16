def choice_num_to_fig(num, who):

  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

  scissors = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''

  if who == 'computer':
    print('Computer chose:')

  if num == 0:
    print(rock)
  elif num == 1:
    print(paper)
  elif num == 2:
    print(scissors)
