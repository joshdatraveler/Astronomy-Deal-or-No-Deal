import game_functions as gf
import simplified_version as sv

game_select = int(input('Enter the game number 1 or 2: '))
if game_select == 1:
  item_list = sv.text_to_code('shortinventory1.txt')
elif game_select == 2:
  item_list = sv.text_to_code('shortinventory2.txt')

print (sv.dealer_offer(item_list))