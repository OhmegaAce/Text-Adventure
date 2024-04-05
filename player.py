def character_creator():
	# Asks user what they want their character to be named
	name = input('What do you want your name to be?: ')

	# returns the values for the character
	return {
		'name': name,
	}


def stats(x):
	character = x
	print()
	print("Character Stats".center(50, '_'))
	print('Name: ' + character['name'])
	print(f"HP: {character['hp']}")
	print(f"Weapon: {character['weapon']['name']}")
	print(f"Weapon Attack: {character['weapon']['atk'][0]}(min), {character['weapon']['atk'][1]}(max)")
	print(f"Armor: {character['armor']['name']}")
	print(f"Defense: {character['armor']['def']}")
	print(f"Gold: {character['gold']}")
	print()
	print('Consumables'.center(50, '_'))
	if len(character['items']) > 0:
		for i in range(len(character['items'])):
			print(character['items'][i]['name'] + f": heals {character['items'][i]['heal']} HP")
	else:
		print('none')
