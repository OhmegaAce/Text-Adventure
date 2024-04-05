import random
import combat
import items
import enemies
import player
import menus

'''
Name: Kole

'''
if __name__ == "__main__":
	print("""\
    #     #                                                 #     #                 
    #  #  #  ####  #####  #      #####      ####  ######    #  #  # # #    # #####  
    #  #  # #    # #    # #      #    #    #    # #         #  #  # # ##   # #    # 
    #  #  # #    # #    # #      #    #    #    # #####     #  #  # # # #  # #    # 
    #  #  # #    # #####  #      #    #    #    # #         #  #  # # #  # # #    # 
    #  #  # #    # #   #  #      #    #    #    # #         #  #  # # #   ## #    # 
     ## ##   ####  #    # ###### #####      ####  #          ## ##  # #    # #####  
                #                     #######                 
               # #   #    # #####     #       # #####  ###### 
              #   #  ##   # #    #    #       # #    # #      
             #     # # #  # #    #    #####   # #    # #####  
             ####### #  # # #    #    #       # #####  #      
             #     # #   ## #    #    #       # #   #  #      
             #     # #    # #####     #       # #    # ###### 
  
      """)
	print()
	print('Select an option from the list below'.center(50, '_'))
	print('1. Start', '\n2. Exit')
	selection = 0
	character = {  # Starting stats for the character
		'name': 'none',
		'hp': 100,
		'weapon': items.stick,
		'armor': items.rags,
		'items': [items.smallpotion],
		'gold': 0,
	}
	while True:
		try:
			# check to make sure that an integer is entered
			selection = int(input())
		except ValueError:
			print()
			print('Please enter a valid list selection')
			print()
			continue
		if selection == 1:
			print("Let's go!")
			print()
			break
		elif selection == 2:
			print('Bye Bye!')
			break
		else:
			print()
			print('Please enter a valid list selection')
			print()

	if selection == 1:
		# Lets the user choose their name and class
		character.update(player.character_creator())
		print()
		print('Welcome, ' + character['name'] + '!')
		print()

	print('Time to fight!')
	print()
	while True:
		try:
			print('Where do you want to go?'.center(50, '_'))
			print('1. Arena')
			print('2. Store')
			print('3. Player Stats')
			print('4. Exit')
			selection = int(input())
		except ValueError:
			print()
			print('Please enter a valid list selection')
			print()
			continue
		if selection == 1:
			arena = menus.arenaSelect()
			if arena == 1:
				character.update(combat.battle(enemies.slime, character))
			elif arena == 2:
				character.update(combat.battle(enemies.skeleton, character))
			elif arena == 3:
				character.update(combat.battle(enemies.zombie, character))
			elif arena == 4:
				character.update(combat.battle(enemies.bear, character))
		elif selection == 2:
			character.update(menus.store(character))
		elif selection == 3:
			player.stats(character)
		elif selection == 4:
			if menus.confirm() == 0:
				break


		if character['hp'] <= 0:
			# if the players health drops to 0 or below the game ends
			print("GAME OVER")
			break