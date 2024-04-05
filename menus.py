import items


def confirm():
	# used to confirm decisions from player
	while True:
		print()
		print("Are you sure?")
		print("Y or N")
		selection = input()
		if selection == 'y' or selection == 'Y':
			return 0
		elif selection == 'n' or selection == 'N':
			return 1
		else:
			continue


def store(x):
	# Store where Player can buy items with earned gold
	print()
	print("Ye Olde Shope".center(50, "="))

	while True:
		selection = 0
		print(f"You currently have {x['gold']} gold")
		print('1. Weapons')
		print('2. Armor')
		print('3. Consumables')
		print('4. Exit')
		try:
			selection = int(input())
		except ValueError:
			print()
			print('Please enter a valid list selection')
			print()
			continue
		if selection == 1:
			print()
			print('Weapons'.center(50, '_'))
			# shows the weapons that are for sale
			print(f"1. {items.dagger['name']}:")
			print(f"  - Attack: {items.dagger['atk']}")
			print(f"  - Cost: {items.dagger['val']} gold")
			print()
			print(f"2. {items.sword['name']}:")
			print(f"  - Attack: {items.sword['atk']}")
			print(f"  - Cost: {items.sword['val']} gold")
			print()
			print('9. Exit')
			while True:
				selection = 0
				try:
					selection = int(input())
				except ValueError:
					print()
					print('Please enter a valid list selection')
					print()
					continue
				if selection == 1:  # Player select dagger
					if x['gold'] >= items.dagger['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.dagger['val']
							# updates weapon
							x['weapon'] = items.dagger
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 2:  # Player selects sword
					if x['gold'] >= items.sword['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.sword['val']
							# updates weapon
							x['weapon'] = items.sword
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 9:
					break
				else:
					continue
		elif selection == 2:
			print('Armor'.center(50, '_'))
			# shows the armor that is for sale
			print(f"1. {items.robe['name']}:")
			print(f"  - Defense: {items.robe['def']}")
			print(f"  - Cost: {items.robe['val']}")
			print()
			print(f"2. {items.leatherarmor['name']}:")
			print(f"  - Defense: {items.leatherarmor['def']}")
			print(f"  - Cost: {items.leatherarmor['val']}")
			print()
			print(f"3. {items.chainarmor['name']}:")
			print(f"  - Defense: {items.chainarmor['def']}")
			print(f"  - Cost: {items.chainarmor['val']}")
			print()
			print(f"4. {items.ironarmor['name']}:")
			print(f"  - Defense: {items.ironarmor['def']}")
			print(f"  - Cost: {items.ironarmor['val']}")
			print()
			print(f"5. {items.steelarmor['name']}:")
			print(f"  - Defense: {items.steelarmor['def']}")
			print(f"  - Cost: {items.steelarmor['val']}")
			print()
			print('9. Exit')
			while True:
				selection = 0
				try:
					selection = int(input())
				except ValueError:
					print()
					print('Please enter a valid list selection')
					print()
					continue
				if selection == 1:  # Player select robe
					if x['gold'] >= items.robe['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.robe['val']
							# updates armor
							x['armor'] = items.robe
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 2:  # Player selects leather
					if x['gold'] >= items.leatherarmor['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.leatherarmor['val']
							# updates armor
							x['armor'] = items.leatherarmor
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 3:  # Player selects chain
					if x['gold'] >= items.chainarmor['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.chainarmor['val']
							# updates armor
							x['armor'] = items.chainarmor
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 4:  # Player selects iron
					if x['gold'] >= items.ironarmor['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.ironarmor['val']
							# updates armor
							x['armor'] = items.ironarmor
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 5:  # Player selects steel
					if x['gold'] >= items.steelarmor['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.steelarmor['val']
							# updates armor
							x['armor'] = items.steelarmor
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 9:
					break
				else:
					continue
		elif selection == 3:
			print('Consumables'.center(50, '_'))
			# shows the consumables that are for sale
			print(f"1. {items.smallpotion['name']}")
			print(f"  - Heal: {items.smallpotion['heal']}")
			print(f"  - Cost: {items.smallpotion['val']}")
			print()
			print(f"2. {items.potion['name']}")
			print(f"  - Heal: {items.potion['heal']}")
			print(f"  - Cost: {items.potion['val']}")
			print()
			print(f"3. {items.largepotion['name']}")
			print(f"  - Heal: {items.largepotion['heal']}")
			print(f"  - Cost: {items.largepotion['val']}")
			print()
			print(f"9. Exit")
			while True:
				selection = 0
				try:
					selection = int(input())
				except ValueError:
					print()
					print('Please enter a valid list selection')
					print()
					continue
				if selection == 1:  # Player select small potion
					if x['gold'] >= items.smallpotion['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.smallpotion['val']
							# updates weapon
							x['items'].append(items.smallpotion)
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				if selection == 2:  # Player select potion
					if x['gold'] >= items.potion['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.potion['val']
							# updates weapon
							x['items'].append(items.potion)
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				if selection == 3:  # Player select large potion
					if x['gold'] >= items.largepotion['val']:
						if confirm() == 0:
							# updates gold amount
							x['gold'] = x['gold'] - items.largepotion['val']
							# updates weapon
							x['items'].append(items.largepotion)
							break
						else:
							break
					else:
						print('You do not have enough money')
						print()
						break
				elif selection == 9:
					break
				else:
					continue
		elif selection == 4:
			return x


def arenaSelect():
	while True:
		print()
		print('Choose Your Opponent'.center(50, '~'))
		print('1. Slime (easy)')
		print('2. Skeleton (medium)')
		print('3. Zombie (hard)')
		print('4. Bear (very hard)')
		try:
			selection = int(input())
		except ValueError:
			print('Select a list option')
			continue
		if 0 < selection <= 4:
			# if an option is chosen from the list, the loop breaks and returns the selection
			return selection
