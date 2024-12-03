from sys import exit
from random import randint
from dialogue import DIALOGUE

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Dungeon(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You're not so good at this.",
        "I have a cat that's better at this.",
        "It's okay, you'll do better next time."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class EntryHall(Scene):
    def enter(self):
        print(DIALOGUE["EntryHall_enter"])
        action = input("Choose a door: [R]ed, [B]lue, or [E]ntrance > ")
        if action == 'b':
            return 'blue_room'
        elif action == 'r':
            return 'red_room'
        elif action == 'e':
            print(DIALOGUE["EntryHall_leave"])
        else:
            print("Does Not Compute.")
            return 'entry_hall'

class BlueRoom(Scene):
    def enter(self):
        print(DIALOGUE["BlueRoom_enter"])
        action = input("Do you [L]eave, [O]pen the treasure chest, or [A]ttack the guard? > ")
        if action in ["leave", "l"]:
            return 'entry_hall'
        elif action in ["open", "o"]:
            print("The chest is empty.")
            return 'entry_hall'
        elif action in ["attack", "a"]:
            print("You defeat the guard.")
            return 'entry_hall'
        else:
            print("Game over.")
            return 'death'

class RedRoom(Scene):
    def enter(self):
        print(DIALOGUE["RedRoom_enter"])
        action = input("Do you [T]ake the suit or [L]eave it? > ")
        if action in ["take", "t"]:
            print("You put the suit of armor on. It fits perfectly.")
            return 'entry_hall'
        elif action in ["leave", "l"]:
            print("You go back to the entrance room.")
            return 'entry_hall'
        else:
            print("Game over.")
            return 'death'
        
class Finished(Scene):
    def enter(self):
        print(DIALOGUE["EntryHall_leave"])
        return 'finished'
            

class Map(object):
    scenes = {
        'entry_hall': EntryHall(),
        'red_room': RedRoom,
        'blue_room': BlueRoom(),
        'death': Death(),
        'finished': Finished
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('entry_hall')
a_game = Dungeon(a_map)
a_game.play()