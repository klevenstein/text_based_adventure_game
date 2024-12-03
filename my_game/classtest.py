import os

class PlayerCharacter:
    def __init__(self, name, pc_class, armor):
        self.name = name
        self.pc_class = pc_class
        self.armor = armor

os.system("clear")

fighter = PlayerCharacter("Lae'zel", "Fighter", "Plate")
wizard = PlayerCharacter("Gale", "Wizard", "Robe")

print("Here is your adventuring party:")
print(f"{fighter.name} is a {fighter.pc_class}, wearing {fighter.armor}.")
print(f"{wizard.name} is a {wizard.pc_class}, wearing {wizard.armor}.")

#    def armor_on(self, protect):
#        protect.armor_on = False

#   def armor(self, protect):
#        if protect.armor_on == True:
#            print("I am wearing armor")
#        if protect.armor_on == False:
#            print("I need armor")
#            gear = input("Should I put on armor > ")
#            if gear in ["y", "yes", "Y"]:
#                protect.armor_on = True
#                print("Now I am wearing armor")
#           else:
#                protect.armor_on = False
#                print("I'm still not wearing armor")

#def fight():
#    print("I am fighting a monster")
#    if protect.armor_on == True:
#        print("I will win!")
#    elif protect.armor_on == False:
#        print("I will lose.")


