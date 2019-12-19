import random
min = 1
max = 6
cpu_score = 0
cpu_diceroll = 0
p2_score = 0
rounds = 1
start_roll = input('Do you want to roll the dice?(y/n)')

if start_roll == 'Yes' or start_roll == 'yes' or start_roll == 'y': 
  print( 'Round ' + str(rounds))
  cpu_diceroll = random.randint(min, max)
  p2_diceroll = random.randint(min, max)
  print('CPU rolled ' + str(cpu_diceroll))
  print('You rolled ' + str(p2_diceroll))
  rounds += 1

  if cpu_diceroll == p2_diceroll:
    print('Draw')
  elif cpu_diceroll > p2_diceroll:
    print('CPU wins!')
    cpu_score =+ 1
  elif cpu_diceroll < p2_diceroll:
    print('You win!')
    p2_score += 1
  print('CPU score: ' + str(cpu_score))
  print('You score: ' + str(p2_score))

start_roll2 = input('Hit enter to start Round ' + str(rounds))

if start_roll2 == 'Yes' or start_roll == 'yes' or start_roll == 'y': 
  print( 'Round ' + str(rounds))
  cpu_diceroll = random.randint(min, max)
  p2_diceroll = random.randint(min, max)
  print('CPU rolled: ' + str(cpu_diceroll))
  print('You rolled: ' + str(p2_diceroll))
  rounds += 1
  
  if cpu_diceroll == p2_diceroll:
    print('Draw')
  elif cpu_diceroll > p2_diceroll:
    print('CPU wins!')
    cpu_score =+ 1
  elif cpu_diceroll < p2_diceroll:
    print('You win!')
    p2_score += 1
  print('CPU score: ' + str(cpu_score))
  print('You score: ' + str(p2_score))

start_roll3 = input('Hit enter to start Round ' + str(rounds))

if start_roll3 == 'Yes' or start_roll == 'yes' or start_roll == 'y': 
  print( 'Round ' + str(rounds))
  cpu_diceroll = random.randint(min, max)
  p2_diceroll = random.randint(min, max)
  print('CPU rolled: ' + str(cpu_diceroll))
  print('You rolled: ' + str(p2_diceroll))
  rounds += 1

  
  if cpu_diceroll == p2_diceroll:
    print('Draw')
  elif cpu_diceroll > p2_diceroll:
    print('CPU wins!')
    cpu_score =+ 1
  elif cpu_diceroll < p2_diceroll:
    print('You win!')
    p2_score += 1
  print('CPU score: ' + str(cpu_score))
  print('You score: ' + str(p2_score))

start_roll4 = input('Hit enter to start Round ' + str(rounds))


if start_roll4 == 'Yes' or start_roll == 'yes' or start_roll == 'y': 
  print( 'Round ' + str(rounds))
  cpu_diceroll = random.randint(min, max)
  p2_diceroll = random.randint(min, max)
  print('CPU rolled: ' + str(cpu_diceroll))
  print('You rolled: ' + str(p2_diceroll))
  rounds += 1

  
  if cpu_diceroll == p2_diceroll:
    print('Draw')
  elif cpu_diceroll > p2_diceroll:
    print('CPU wins!')
    cpu_score =+ 1
  elif cpu_diceroll < p2_diceroll:
    print('You win!')
    p2_score += 1
  print('CPU score: ' + str(cpu_score))
  print('You score: ' + str(p2_score))

start_roll5 = input('Hit enter to start Round ' + str(rounds))


if start_roll5 == 'Yes' or start_roll == 'yes' or start_roll == 'y': 
  print( 'Round ' + str(rounds))
  cpu_diceroll = random.randint(min, max)
  p2_diceroll = random.randint(min, max)
  print('CPU rolled: ' + str(cpu_diceroll))
  print('You rolled: ' + str(p2_diceroll))
  rounds += 1

  
  if cpu_diceroll == p2_diceroll:
    print('Draw')
  elif cpu_diceroll > p2_diceroll:
    print('CPU wins!')
    cpu_score =+ 1
  elif cpu_diceroll < p2_diceroll:
    print('You win!')
    p2_score += 1
  print('CPU score: ' + str(cpu_score))
  print('You score: ' + str(p2_score))