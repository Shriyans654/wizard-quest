import random
from random import randint, choice

print(
    """
     .->     _       (`-')   (`-')  _    (`-') _(`-')   
 (`(`-')/`) (_)      ( OO).->(OO ).-/ <-.(OO )( (OO ).->
,-`( OO).', ,-(`-'),(_/----. / ,---.  ,------,)\    .'_ 
|  |\  |  | | ( OO)|__,    | | \ /`.\ |   /`. ''`'-..__)
|  | '.|  | |  |  ) (_/   /  '-'|_.' ||  |_.' ||  |  ' |
|  |.'.|  |(|  |_/  .'  .'_ (|  .-.  ||  .   .'|  |  / :
|   ,'.   | |  |'->|       | |  | |  ||  |\  \ |  '-'  /
`--'   '--' `--'   `-------' `--' `--'`--' '--'`------' 
 <-.(`-')              (`-')  _ (`-').->(`-')           
  __( OO)       .->    ( OO).-/ ( OO)_  ( OO).->        
 '-'---\_) ,--.(,--.  (,------.(_)--\_) /    '._        
|  .-.  |  |  | |(`-') |  .---'/    _ / |'--...__)      
|  | | <-' |  | |(OO )(|  '--. \_..`--. `--.  .--'      
|  | |  |  |  | | |  \ |  .--' .-._)   \   |  |         
'  '-'  '-.\  '-'(_ .' |  `---.\       /   |  |         
 `-----'--' `-----'    `------' `-----'    `--'
"""
)


def print_bar():
    print("=============")


print_bar()
player_name = input("What is your name?")

print(f"Welcome, {player_name}! Let the Wizard Quest begin.")


def get_input():
    print_bar()
    print("Actions")
    print_bar()
    print(choices)
    player_choice = input("What do you want to do?")
    return player_choice


def show_player_stats():
    print_bar()
    print(
        f"""
        {player_name}
        =======
        HEALTH: {player["health"]}
        POTIONS: {player["potions"]}
        GOLD: {player["gold"]}
        """
    )


def get_loot():
    luck = random.randint(0, 3)
    if luck < 3:
        loot = random.randint(100, 1000)
        print(f"You found {loot} gold!")
        player["gold"] += loot
    else:
        print("You found a healing potion")
        player["potions"] += 1


def start_combat():
    creatures = ["orc", "troll", "skeleton knight", "thief", "cave spider"]
    enemy = random.choice(creatures)
    print(f"A {enemy} jumped out from a hidden alcove!")
    enemy_health = random.randint(1, 3)
    while enemy_health > 0:
        attack = random.randint(0, 3)
        if attack == 0:
            print(
                "You swung your sword but completely missed. You take 1 damage."
            )
            player["health"] -= 1
        else:
            print(f"You struck the {enemy} for {attack} damage")
            enemy_health -= attack
        if player["health"] <= 0:
            return
    print(f"You defeated the {enemy}! You search its remains for some sweet loot.")
    get_loot()


def search():
    luck = random.randint(0, 2)
    if luck == 0:
        print("You were injured by a trap!")
        player["health"] -= 1
    elif luck == 1:
        print("You found some gold.")
    elif luck == 5:
        get_loot()
    elif luck == 3 or luck == 6:
        print("You were attacked!")
        start_combat()

    else:
        print("You search the room but found nothing")


def heal():
    if player["potions"] > 0:
        heal_amount = random.randint(1, 3)
        player["health"] += heal_amount
        player["potions"] -= 1
        print(f"You used a healing potion and gained {heal_amount} health.")
    else:
        print("You are out of potions.")


player = {
    "health": 10,
    "potions": 3,
    "gold": 0,
}

choices = ["move on", "search", "heal", "quit"]

from rooms import create_room

rooms = 0

while True:
    show_player_stats()
    room = create_room()
    print(room)
    action = get_input()
    if action == "quit":
        break
    elif action == "move on":
        print("You move on to the next room...")
    elif action == "search":
        print("You searched the room")
        search()
    elif action == "heal":
        heal()
        print("You've gained one health.")
    print(f"You chose to {action}.")
    input("Please enter to continue")
    rooms += 1
    
    if player["health"] <= 0:
        print("You were too injured to keep going...")
        break

print(f"You made it through {rooms} rooms")
print(f"You found {player['gold']} gold coins")

print(
    """
 ______ _______ _______ _______       _____  _    _ _______  ______
|  ____ |_____| |  |  | |______      |     |  \  /  |______ |_____/
|_____| |     | |  |  | |______      |_____|   \/   |______ |    \_
"""
)
