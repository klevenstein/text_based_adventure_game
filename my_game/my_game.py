import os

def fight():
    print("Your opponent attacks you with everything they have!")
    fight_response = input("Do you [F]ight back or [R]un away? > ")
    if fight_response in ["fight", "f"]:
        print("You are too easily overpowered by the guard. If you keep fighting, you will probably lose.")
        fight_continue = input("You can [C]ontinue to fight, or [R]un away. > ")
        if fight_continue in ["continue", "c"]:
            print("The guard knocks you down and the last thing you see is a sword descending toward your face.")
            end_adventure_dead()
        if fight_continue in ["run", "r"]:
            print("Discretion is the better part of valour.")
            print("You get away! ... and end up where you started.")
            choose_door()
    elif fight_response in ["run", "r"]:
        print("The best fights are the ones you don't start.")
        print("You get away! ... and end up where you started.")
        choose_door()

def treasure_chest():
    import game_dict
    print("You open the treasure chest.")
    print("Inside, you see the following items:")
    for x in game_dict.treasure:
        print(x)
    loot = input("Will you take the [G]old, the [C]up, the [R]ing, or the [S]word? > ")
    if loot in ["gold", "g"]:
        print("The coins are shiny and smooth. You put them in your pocket.")
        game_dict.treasure.remove("Gold coins")
        blue_room()
    elif loot in ["cup", "c"]:
        print("You see now that the cup is actually badly tarnished. In fact, it's only plate.")
        loot_cup = input("Do you [L]eave it or [T]ake it? > ")
        if loot_cup in ["leave", "l"]:
            print("You put it back.")
            blue_room()
        if loot_cup in ["take", "t"]:
            print("You take the cup anyway and go.")
            game_dict.treasure.remove("A silver cup")
            blue_room()
    elif loot in ["ring", "r"]:
        print("The ring is curiously heavy for its size.")
        print("You feel compelled to stick it in your pocket.")
        print("You do so, and feel uneasy. Maybe you should put it back?")
        game_dict.treasure.remove("A diamond ring")
        loot_ring = input("Do you [R]eturn the ring, or [K]eep it? > ")
        if loot_ring in ["return", "r"]:
            print("You put the ring back and feel better.")
            game_dict.treasure.add("A diamond ring")
        if loot_ring in ["keep", "k"]:
            print("You decide to keep the ring anyway.")
            print("After all, why shouldn't you keep it?")
            print("It's yours now. Your precious.")
        blue_room()
    elif loot in ["sword", "s"]:
        game_dict.treasure.remove("A steel sword")
        print("As you pick up the sword, the guard wakes up and takes a swing at you!")
        fight()
    else:
        print("Don't care much for material goods, huh?")
        blue_room()

def red_room():
    print("It's a red room.")
    print("It's not finished yet. Go back.")
    choose_door()

def yellow_room():
    print("You pass through the door ... and end up where you started.")
    choose_door()

def blue_room():
    
    print("You are inside a room where the walls, ceiling, and floor are all painted blue.")
    print("There is a treasure chest to the right and a sleeping goblin guard to the left.")
    blue_action = input("Do you [L]eave, [O]pen the treasure chest, or [A]ttack the guard? > ")
    if blue_action in ["leave", "l"]:
        start_adventure()
    elif blue_action in ["open", "o"]:
        treasure_chest()
    elif blue_action in ["attack", "a"]:
        print("The guard wakes up and swings a sword at you!")
        fight()
    else:
        print("Come on, make a decision.")
        blue_room()

def start_adventure():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Beginning Adventurer's Dungeon.\n")
    print("You open the creaking wooden door and enter a room.")
    print("On your left is a red door, and on your right is a blue door.") 
    print("In front of you is a yellow door.")
    print("Behind you is the wooden door where you came in.")
    choose_door()

def choose_door():
    door_picked = input("Which door do you pick? [R]ed, [B]lue, [Y]ellow], or [E]ntrance > ")
    if door_picked in ["red","r"]:
        red_room()
    elif door_picked in ["blue","b"]:
        blue_room()
    elif door_picked in ["yellow","y"]:
        yellow_room()
    elif door_picked in ["entrance", "e"]:
        end_adventure()
    else:
        print("Enter one of the letters in the list.")
        choose_door()

def end_adventure():
    print("You go back out through the creaking wooden door and stand blinking in the sunlight.")
    print("Your adventure is over, for now.")
    print("\nThe end.\n Thanks for playing!")

def end_adventure_dead():
    print("You have died.")
    print("\nThe end.\n Thanks for playing!")

def main():
    os.system("clear")
    player_name = get_player_name()
    start_adventure()

def get_player_name():
    name = input("What's your name, player? > ")
    alt_name = "Daisy Dewdrop Fluffington"
    answer = input(f"Thanks, {alt_name}. That is your name, right? [Y/N] > ")
    if answer.lower() in ["y","yes"]:
        name = alt_name
        print(f"Aha, a fellow Baldur's Gate fan. Let's go, {name}!")
    elif answer.lower() in ["n","no"]:
        print(f"Okay, fine, {name}. Killjoy. Let's go anyway.")
    else:
        print(f"Very funny, {alt_name}. Let's go.")
        name = alt_name

if __name__ == '__main__':
    main()