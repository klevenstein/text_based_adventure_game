import os

def fight():
    print("Your opponent attacks you with everything they have!")
    fight_response = input("Do you [F]ight back or [R]un away?")
    if fight_response in ["fight", "f"]:
        print("You win!")
        end_adventure()
    elif fight_response in ["run", "r"]:
        print("You get away! ... and end up where you started.")
        start_adventure()

def red_room():
    print("It's a red room.")
    start_adventure()

def yellow_room():
    print("You pass through the door ... and end up where you started.")
    start_adventure()

def blue_room():
    import game_dict
    
    print("It's a blue room.")
    print("There is a treasure chest to the right and a sleeping goblin guard to the left.")
    blue_action = input("Do you [L]eave, [O]pen the treasure chest, or [A]ttack the guard?")
    if blue_action in ["leave", "l"]:
        start_adventure()
    elif blue_action in ["open", "o"]:
        print("You open the treasure chest.")
        print("Inside, you see the following items:")
        for x in game_dict.treasure:
            print(x)
        loot = input("Will you take the [G]old, the [C]up, the [R]ing, or the [S]word?")
        if loot in ["gold", "g"]:
            print("The coins are shiny and smooth. You put them in your pocket and leave.")
            start_adventure()
        elif loot in ["cup", "c"]:
            print("You see now that the cup is actually badly tarnished. In fact, it's only plate.")
            print("You put it back and leave.")
            start_adventure
        elif loot in ["ring", "r"]:
            print("The ring is curiously heavy for its size.")
            print("You feel compelled to stick it in your pocket.")
            print("You do so, and leave.")
            start_adventure()
        elif loot in ["sword", "s"]:
            print("As you pick up the sword, the guard wakes up and takes a swing at you!")
            fight()
        else:
            print("Don't care much for material goods, huh?")
            blue_room()
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
    door_picked = input("Which door do you pick? [R]ed, [B]lue, [Y]ellow], or [E]ntrance >")
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
        print("Okay, fine, {name}. Killjoy. Let's go anyway.")
    else:
        print(f"Very funny, {alt_name}. Let's go.")
        name = alt_name

if __name__ == '__main__':
    main()