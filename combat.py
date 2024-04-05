import random
import items


def battle(enemy, character):
	# Using this function, the user will be able to battle multiple enemies and gain exp
	# New creatures are easily able to be added
	# Saves enemy info from the dictionary to seperate variables for easy access

	print()
	print('Battle Start!'.center(50, '_'))

	print(f"You are fighting a(n) {enemy['name']}")
	enemyhp = enemy['hp']
	while enemyhp > 0:
		selection = 0
		print(f"{enemy['name']} HP: {enemyhp}")
		print('1. Attack')
		print('2. Use Item')
		while True:
			try:
				selection = int(input('Selection: '))
				break
			except ValueError:
				print('Please enter a number')
				continue
		if selection == 1:
			# This is the player attack
			randatk = random.randint(character['weapon']['atk'][0], character['weapon']['atk'][1])
			total_dmg = randatk - enemy['def']
			enemyhp = enemyhp - total_dmg
			print()
			print(f"** you did {total_dmg} damage **")
			print()
			print(f"*** {enemy['name']} has {enemyhp} HP left ***")
			print()
		elif selection == 2 and len(character['items']) > 0 and character['hp'] < 100:
			# This is where the player can use an item
			print('Use what Item?')
			for i in range(len(character['items'])):
				print(f"{i}. {character['items'][i]['name']}")
				print(f"  - Heal: {character['items'][i]['heal']}")
			while True:
				try:
					selection = int(input())
					break
				except ValueError:
					print('Please enter a number')
					continue
			character['hp'] = character['hp'] + character['items'][selection]['heal']
			if character['hp'] > 100:
				# This is so the player can't overheal
				character['hp'] = 100
			print()
			print(f"** you healed {character['items'][selection]['heal']} HP **")
			print()
			print(f"*** your HP is now at {character['hp']}")
			del character['items'][selection]
		elif selection == 2 and len(character['items']) == 0:
			print()
			print("You have no items")
			print()
			continue
		elif selection == 2 and character['hp'] == 100:
			print()
			print("You are at max health")
			print()
			continue
		if enemyhp > 0:
			# This is the enemy attack
			print('Enemy Turn')
			print()
			randatk = random.randint(enemy['atk'][0], enemy['atk'][1])
			total_dmg = randatk - character['armor']['def']
			if total_dmg >= 0:
				# if the damage the enemy does ends up being a negative number, the total will default to 0
				# so no negative damage (which heals the player) is done
				character['hp'] = character['hp'] - total_dmg
			else:
				total_dmg = 0
			print()
			print(f"** {enemy['name']} did {total_dmg} damage **")
			print()
			print(f"*** You have {character['hp']} HP left ***")
			print()
			if character['hp'] <= 0:
				return character
		else:
			rand_gold = random.randint(enemy['gold'][0], enemy['gold'][1])
			print(f'You won this battle! You will gain {rand_gold} gold')

			character['gold'] = character['gold'] + rand_gold

	return character
