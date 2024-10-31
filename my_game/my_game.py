import os
import game_dict

# Status of player and setting at the beginning of the game

wearing_armor = False
guard_alive = True
carrying_sword = False

def fight():
    global guard_alive
    fight_response = input("Do you [F]ight back or [R]un away? > ")
    if fight_response in ["fight", "f"] and wearing_armor == False and carrying_sword == False:
        print("You are too easily overpowered by the guard. If you keep fighting, you will probably lose.")
        fight_continue = input("Will you [C]ontinue to fight, or [R]un away? > ")
        if fight_continue in ["continue", "c"]:
            print("The guard knocks you down and the last thing you see is a sword descending toward your face.")
            end_adventure_dead("You have been defeated by a goblin.")
        if fight_continue in ["run", "r"]:
            print("Discretion is the better part of valour.")
            print("You get away! ... and end up where you started.")
            choose_door()
        else:
            print("Make a choice!")
            fight()
    if fight_response in ["fight", "f"] and wearing_armor == True and carrying_sword == False:
        print("The guard's attacks bounce off your armor, but you have no way of fighting back.")
        print("The smart thing to do now is run, and you get away.")
        choose_door()
    if fight_response in ["fight", "f"] and wearing_armor == False and carrying_sword == True:
        print("You and the guard engage in a fierce sword fight!")
        print("But although you have a superior sword, you have no armor.")
        print("The guard stabs you!")
        end_adventure_dead("You have been defeated by a goblin.")
    if fight_response in ["fight", "f"] and wearing_armor == True and carrying_sword == True:
        print("You and the guard engage in a fierce sword fight!")
        print("Your sword is superior and you win!")
        guard_alive = False
        blue_room()
    elif fight_response in ["run", "r"]:
        print("The best fights are the ones you don't start.")
        print("You get away! ... and end up where you started.")
        choose_door()

def treasure_chest():
    global carrying_sword
    print("You open the treasure chest.")
    print("Inside, you see the following items:")
    for x in game_dict.treasure:
        print(x)
    loot = input("Which do you take? Or, you can close the chest by pressing [X]. > ")
    if loot in ["gold", "g"]:
        print("The coins are shiny and smooth. You put them in your pocket.")
        game_dict.treasure.remove("[G]old coins")
        game_dict.inventory.add("Gold coins")
        treasure_chest()
    elif loot in ["cup", "c"]:
        print("You see now that the cup is actually badly tarnished. In fact, it's only plate.")
        loot_cup = input("Do you [L]eave it or [T]ake it? > ")
        if loot_cup in ["leave", "l"]:
            print("You put it back.")
            treasure_chest()
        if loot_cup in ["take", "t"]:
            print("You take the cup anyway.")
            game_dict.treasure.remove("A silver [C]up")
            game_dict.inventory.add("A silver cup")
            treasure_chest()
    elif loot in ["ring", "r"]:
        print("The ring is curiously heavy for its size.")
        print("You feel compelled to stick it in your pocket.")
        print("You do so, and feel uneasy. Maybe you should put it back?")
        game_dict.treasure.remove("A diamond [R]ing")
        loot_ring = input("Do you [R]eturn the ring, or [K]eep it? > ")
        if loot_ring in ["return", "r"]:
            print("You put the ring back and feel better.")
            game_dict.treasure.add("A diamond [R]ing")
        if loot_ring in ["keep", "k"]:
            print("You decide to keep the ring anyway.")
            print("After all, why shouldn't you keep it?")
            print("It's yours now. Your precious.")
            game_dict.inventory.add("A diamond ring")
        treasure_chest()
    elif loot in ["sword", "s"]:
        game_dict.treasure.remove("A steel [S]word")
        game_dict.inventory.add("A steel sword")
        carrying_sword = True
        print("As you pick up the sword, the guard wakes up and takes a swing at you!")
        fight()
    else:
        print("Don't care much for material goods, huh? You close the chest.")
        blue_room()

def red_room():
    global wearing_armor
    if wearing_armor == False:
        print("The walls, ceiling, and floor of this room are made out of red marble.")
        print("There is a suit of armor on a table in the middle of the room.")
        choice = input("Do you [T]ake the suit or [L]eave it? > ")
        if choice in ["take", "t"]:
            print("You put the suit of armor on.")
            print("It fits perfectly.")
            print("You go back to the entrance room.")
            wearing_armor = True
            game_dict.inventory.add("Armor")
            choose_door()
        elif choice in ["leave", "l"]:
            print("You go back to the entrance room.")
            choose_door()
        else:
            print("Make up your mind.")
            red_room()
    if wearing_armor == True:
        print("There is nothing in this room anymore.")
        print("You go back to the entrance room.")
        choose_door()

def yellow_room():
    print("You pass through the door ... and end up where you started.")
    choose_door()

def blue_room():
    global guard_alive
    print("You are inside a room where the walls, ceiling, and floor are all painted blue.")
    if guard_alive == True:
        print("There is a treasure chest to the right and a sleeping goblin guard to the left.")
        choice = input("Do you [L]eave, [O]pen the treasure chest, or [A]ttack the guard? > ")
    if guard_alive == False:
        print("There is a treasure chest and the remains of an unfortunate goblin guard on the floor.")
        choice = input("Do you [L]eave or [O]pen the treasure chest > ")
    if choice in ["leave", "l"]:
        choose_door()
    elif choice in ["open", "o"]:
        treasure_chest()
    elif choice in ["attack", "a"]:
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

def inventory():
    print("You are currently carrying:")
    for x in game_dict.inventory:
        print(x)
    choose_door()

def choose_door():
    choice = input("Check your [I]nventory or choose a door: [R]ed, [B]lue, [Y]ellow], or [E]ntrance > ")
    if choice in ["red","r"]:
        red_room()
    elif choice in ["blue","b"]:
        blue_room()
    elif choice in ["yellow","y"]:
        yellow_room()
    elif choice in ["entrance", "e"]:
        end_adventure()
    elif choice in ["inventory", "i"]:
        inventory()
    else:
        print("Enter one of the letters in the list.")
        choose_door()

def end_adventure():
    print("You go back out through the creaking wooden door and stand blinking in the sunlight.")
    print("Your adventure is over, for now.")
    print("The end.\nThanks for playing!")
    exit(0)

def end_adventure_dead(why):
    print(why, "\nYou have died.")
    print("The end.\nThanks for playing!")
    exit(0)

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