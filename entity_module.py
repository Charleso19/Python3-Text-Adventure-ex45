from random import randint

"""This module consist of the the single class below."""


class CreateEntity(object):


    """The class is used to contruct an 'entity', i.e. a player or an enemy."""

    def __init__(self):
        """
        I've set some of the attributes to random integers so the combat
        system is not always the same.
        """
        self.attack = randint(1,3)
        self.defence = randint(1,3)
        self.hp = 100
        self.inventory = {}

    def view_entity(self):
        """
        This method is used to view the player's stats during the game,
        although an enemy instance of this class also inherits this method,
        it is is never called.
        """
        print("Your current stats are:")
        print(f"Attack: {self.attack}")
        print(f"Defence: {self.defence}")
        print(f"Health: {self.hp}")
        print("\nInventory:")

        if self.inventory == {}:
            print("Your inventory is currently empty.")

        else:
            print("Item:        Power:")

            for key, val in self.inventory.items():
                print(f"{key}         {val}")
