import random as rand


#sets the class for the items appearing in each case
class Space_Item:
  def __init__(self,case,name,desc,fun_fact,price):
    self.case = case
    self.name = name
    self.desc = desc
    self.fun_fact = fun_fact
    self.price = price
  def __repr__(self):
    return '{},{},{},{},{}'.format(self.case,self.name,self.desc,self.fun_fact,self.price)

#function that facilitates the creation of items for each list
def add_item():
  selectgame = int(input('Enter which game this item is for (1 or 2): '))
  case = 0
  name = input ('Enter item name: ')
  desc = input ('Enter short description: ')
  fact = input ('Enter a fun fact: ')
  price = float(input('Enter the approximate price of the item: '))
  new_item = Space_Item(case,name,desc,fact,price)
  print (new_item)
  if selectgame == 1:
    with open('inventory.txt', 'a') as f:
      f.write('\n'+ str(new_item))
  elif selectgame == 2:
    with open('inventory2.txt', 'a') as f:
      f.write('\n'+ str(new_item))
  else:
    print ('That game is not avaiable')

#takes the items from the text file and converts them back to usable class instances
def text_to_code():
  item_list = []
  inv = open(txtfile, 'r')
  lines = inv.readlines()
  for item in lines:
    item_data = item.split(',')
    #turning the keywords string back into a list
    #print (item_data)
    case = int(item_data[0])
    name = item_data[1]
    desc = item_data[2]
    fact = item_data[3]
    price = float(item_data[4])
    item_class = Space_Item(name,desc,price,inv,keyword)
    #print (item_class)
    item_list.append(item_class)
  return item_list

#randomizes case numbers for each item on game set up
def game_set(item_list):
  case_numbs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  for item in item_list:
    cur_case_numb = random.choice(case_numbs)
    item[0] = cur_case_numb
    case_numbs.pop(cur_case_numb)
  return item_list


        
    