import random
print("\n====================================================")
print("     **********  Welcome to Dungeon  **********")
print("====================================================\n\n")

enemies = ["Skeleton" , "Assassian" , "Vampire" , "BigFoot"]

player_health = 100
number_of_potions = 4
health_potion = 30
enemy_drop_chance = 50
enemy_kill_count = 0
player_input1 = ""

while True :
    enemy = random.choice(enemies)
    enemy_health = random.randint(10 , 76)
    print("====================================================")
    print(f"   **********  {enemy} has appeared  **********")
    print(f"Your HP : {player_health}")
    print(f"{enemy}'s HP : {enemy_health}")
    print("====================================================\n\n")
    while enemy_health > 1 :
        print("====================================================")
        print("What do you want to do?  ")
        print("1. Attack")
        print("2. Drink Health Potion")
        print("3. Run")
        player_input = input("Enter Your Move : ")
        if player_input == "1" :
            enemy_damage = random.randint(10 , 40)
            player_damage = random.randint(0 , 40)
            enemy_health = enemy_health - enemy_damage
            player_health = player_health - player_damage
            print(f"You caused the {enemy} {enemy_damage} damage in the attack...")
            print(f"In retaliational...You caused {player_damage} damage to yourself.!!\n")
            print(f"Your HP : {player_health}")
            print(f"{enemy}'s HP : {enemy_health}")
            if player_health < 1 :
                print("You are too weak to battle now.!!\nYou are brought out of game.!!")
                break
        elif player_input == "2" :
            if number_of_potions > 0 :
                print("You drank a potion...")
                player_health = player_health + health_potion
                number_of_potions = number_of_potions - 1
                print(f"\nYour HP : {player_health}")
                print(f"You now have {number_of_potions} number of potions left...")
            else :
                print("You do not have a single potion..!!")
                print("You must kill an enemy in order to get a potion..")
        elif player_input =="3" :
            print(f"You ran away from the {enemy}...")
            break
        else :
            print("Invalid Command! Enter 1,2 or 3.")

    if player_health < 0 :
        print("\nThank you for playing Dungeon!\nYou did your best!!")
        break

    if enemy_health < 0 :
        print(f"You defeated the {enemy}...")
        print("====================================================\n")
        enemy_kill_count = enemy_kill_count + 1
        if random.randint(0 , 100) > enemy_drop_chance :
            print("====================================================")
            print(f"{enemy} dropped a potion...")
            number_of_potions = number_of_potions + 1
            print(f"You have {number_of_potions} number of potions with you...")
            print("====================================================\n")
    if enemy_kill_count == 3 :
        while True :
            print("What do you want to do?")
            print("1. Continue Fighting")
            print("2. Exit")
            player_input1 = input("Enter your move : ")
            if player_input1 == "1" :
                print("Okay!")
                enemy_kill_count = 0
                break
            elif player_input1 == "2" :
                print("You are successfully brought to a safe place...")
                break
            else :
                print("Invalid Command!")
    if player_input1 == "2" :
        print("\nThank you for playing Dungeon!\nYou did your best!!\n")
        break