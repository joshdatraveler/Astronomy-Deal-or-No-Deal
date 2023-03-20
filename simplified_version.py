import math as math

#speed version of previous sections

class Space_Item():
  def __init__(self, name, price,case):
    self.name = name
    self.price = price
    self.case = case
  def __repr__(self):
    return '{},{},{}'.format(self.name,self.price,self.case)

#adds items to one of 2 lists (2 games were played, 2 sets of items for simplicity)
def add_item():
  selectgame = int(input('Enter which game this item is for (1 or 2): '))
  case = int(input('Enter case number'))
  name = input ('Enter item name: ')
  price = float(input('Enter the approximate price of the item: '))
  new_item = Space_Item(name,price,case)
  print (new_item)
  if selectgame == 1:
    with open('shortinventory1.txt', 'a') as f:
      f.write('\n'+ str(new_item))
  elif selectgame == 2:
    with open('shortinventory2.txt', 'a') as f:
      f.write('\n'+ str(new_item))
  else:
    print ('That game is not avaiable')

#takes the data from the text files and turns them back into a class
def text_to_code(textfile):
  item_list = []
  inv = open(textfile, 'r')
  lines = inv.readlines()
  for item in lines:
    item_data = item.split(',')
    #turning the keywords string back into a list
    #print (item_data)
    name = item_data[0]
    price = float(item_data[1])
    case = int(item_data[2])
    #item_class = Space_Item(name,price,case)
    item_class = [name,price,case]
    #print (item_class)
    item_list.append(item_class)
  return item_list

#scrapped code that automates the process of case entering that was not able to completed fast enough (will complete for future club meetings)
def game_set(item_list):
  user_case = int(input('Enter the user intial case selection: '))
  for item in item_list:
    if item[2] == user_case:
      user_item = item
      item_list.remove(item)
  with open('game1log.txt', 'a') as f:
    f.write('\nUsers case: '+ str(user_item))

  player_done = False
  case_pick_amount = 5
  case_picked_round = 0
  while player_done == False:
    pass
      
      
    '''
    #starting the game
    round = int(input('Which round is this(if initial case pick, type 19):'))
    if round == 19:
      user_case = int(input('Enter the user intial case selection: '))
      for item in item_list:
        if item[2] == user_case
        user_item = item
        item_list.remove(item)
      with open('game1log.txt', 'a') as f:
        f.write('\nUsers case: '+ str(user_item))
    elif round == 1:
      #eliminate 4 in round 1
      count = 4
      while count > 0:
        case_guess = int(input('Enter the first case guessed: '))
        for item in item_list:
          if item[2] == case_guess:
    '''

#simple code that takes the game list and prompts for each case that has been picked. It returns an offer based on remaining case values 
def dealer_offer(item_list):
  cases_picked = int(input('How many cases have been picked(not incuding the players kept case): '))
  case_edit = -1
  while case_edit != cases_picked:
    user_case = int(input('Enter the ' +str(case_edit+1)+ ' case selection(case 0 is the players case): '))
    for item in item_list:
      if item[2] == user_case:
        item_list.remove(item)
    case_edit += 1

  sqrd_avg = []
  for item in item_list:
    sqrdprice = math.sqrt(item[1])
    sqrd_avg.append(sqrdprice)

  tot = float(round(sum(sqrd_avg),0))
  list_len = float(len(sqrd_avg))
  avg = tot/list_len
  dealers_offer = math.sqrt(avg)
  return dealers_offer
      
        
