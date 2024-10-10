# Programmers:  Laure Patera
# Course:  CS151, Professor Zee
# Due Date: 10/9/2024
# PA Assignment: 01
# Problem Statement: this program takes a user through a text adventure game where they can pick a pet
# Data In: type of pet, type of food, name of pet, how many of said pet
# Data Out:  amount of budget remaining, story options depending on input
# Credits: This code is based on the example in the read me file

#output introduction to game and story to the user
print('Welcome to the pet store text adventure game!')
print('You are walking into a pet store with your friend and considering buying a new pet together. \nYour friend is buying the pet, but you will be buying the supplies with a budget of $50.\nOn the side closest to you there are walls of fish, but towards the opposite side of the store \nare aisles with cages of various rodents and birds.')
budget = float(50)

#Ask user which pet they would like to get, and error checking
pet_type = str(input('Please enter the number of the option you like the most as an integer\n\tOption 1: Get a betta\n\tOption 2: Get a guinea pig\n\tOption 3: Come back another day'))
while pet_type != '1' and pet_type != '2' and pet_type != '3':
    print('Invalid answer. Please try again.')
    pet_type = str(input('Please enter the number of the option you like the most as an integer\n\tOption 1: Get a guinea pig\n\tOption 2: Get a betta\n\tOption 3: Come back another day'))

#Story segment for if the user chooses to buy a betta
if pet_type == '1':
    name = str(input('Aww what are you naming it?'))
    if not name.isalpha():
        print('I''m not sure I can pronounce that.')
    else:
        print(name, 'is the perfect name!')

#Asks user which food they would like to buy, affecting the budget
    print('Now you have to decide between food. These are the options on the shelf in front of you.\n\t Food 1: Costs $10.25 and', name, 'is already used to eating it.\n\tFood 2: Costs $3.99 and is the cheapest option if you want to save.\n\tFood 3: Costs $15.75 and has a three-month supply, which is much more than either other option.')
    food1 = 10.25
    food2 = 3.99
    food3 = 15.75
    food_type = str(input(f'Which food would you like to buy for {name}? Please enter the number of the food you like the most as an integer'))
    while food_type != '1' and food_type != '2' and food_type != '3':
        print('Invalid answer. Please try again.')
        food_type = str(input(f'Which food would you like to buy for {name}? Please enter the number of the food you like the most as an integer'))
    if food_type == '1':
        food_type = food1
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')
    elif food_type == '2':
        food_type = food2
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')
    elif food_type == '3':
        food_type = food3
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')

#Story segment for if the user chooses to buy guinea pig(s)
elif pet_type == '2':
    guinea_pig_number = int(input('Nice! How many guinea pigs do you want to get?'))
    if guinea_pig_number >= 5 or guinea_pig_number <= 1:
        print('Are you sure that''s a good idea?')
    else:
       print('That sounds like a good number!')

# Asks user which food they would like to buy, affecting the budget
    print('Now you have to decide between food. These are the options on the shelf in front of you.\n\tFood 1: Costs $12.85 and the guinea pigs are already used to eating it.\n\tFood 2: Costs $5.99 and is the cheapest option if you want to save.\n\tFood 3: Costs $20.75 and has a three-month supply, which is much more than either other option.')
    food1 = 12.85
    food2 = 5.99
    food3 = 20.75
    food_type = str(input(f'Which food would you like to buy? Please enter the number of the food you like the most as an integer'))
    while food_type != '1' and food_type != '2' and food_type != '3':
        print('Invalid answer. Please try again.')
        food_type = str(input(f'Which food would you like to buy? Please enter the number of the food you like the most as an integer'))
    if food_type == '1':
        food_type = food1
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')
    elif food_type == '2':
        food_type = food2
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')
    elif food_type == '3':
        food_type = food3
        budget = budget - food_type
        print('You have $', budget, 'left that you could spend.')

#Story segment for if the user chooses to come back another day
elif pet_type == '3':
    print('You may not have gotten a new pet, but you saved money and avoided a potentially hasty decision.')

