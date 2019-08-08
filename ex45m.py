# As well as built-in modules, I have imported two self-made modules,
# mainly to shorten the current python file and improve readabiltiy

from sys import exit
from random import randint, randrange, choice
from math import sqrt
from textwrap import dedent

from entity_module import CreateEntity
from attack_module import Attack


class Blackboard(object):


    """
    This class is to display the controls of the game. I have named it as a
    blackboard, as the centre of the game (i.e. the HouseRoom), has a blackboard
    on the wall that displays the controls.
    """

    def view_controls(self):

        print(dedent("""
              DIRECTIONS:
              • 'north'
              • 'east'
              • 'south'
              • 'west'

              ACTIONS:
              • 'check case': Checks the trophy case
              • 'examine'/'look': Examines the object
              • 'attack': Attacks an enemy
              • 'stats': View player's stats
              """))



class TreasureCase(object):


    """
    The TreasureCase is styled in a composition format; i.e. the HouseRoom
    has-a TreasureCase. I thought this composition format made more sense.
    N.B. a possible annoyance is that the user must initiate the check_case
    method below in order to win the game.
    """

    treasure = []

    def check_case(self):

        print("Checking treasure in case...")
        print("You have the following treasure:")

        for i in TreasureCase.treasure:
            print(f"• {i}")

        if len(TreasureCase.treasure) >= 3:
            return 'end_room'

        else:
            pass


class HouseRoom(object):

    """
    This is the main central hub of the game, it is where the game starts and
    where access to all other rooms are available.
    """

    def __init__(self):
        """
        I've set this so that the HouseRoom has-a treasure-case and has-a
        blackboard. It seemed easier to work with this way.
        """
        self.treasure_case = TreasureCase()
        self.controls = Blackboard()

    def activate(self, player, troll):
        """
        This is basically the same as the enter() function from exercise 43.
        The Engine object below however passes the player and troll
        (CreateEntity()) objects to every room's activate, often unnecessarily;
        perhaps there is a better way to do this.
        """

        print(dedent("""
              A short sharp sound crackles through the air. Groggy you awake,
              slowly; a pale cold light shines through cracks in the ceiling
              above you.
              What do you do?
              """))

        answer = input("> ")

        if answer == 'north':

            return 'troll_room'

        elif answer == 'east':

            return 'death_room'

        elif answer == 'south':

            return 'gallery_room'

        elif answer == 'west':
            print(dedent("""
                  The door is locked.
                  """))

            return 'house_room'

        elif ("examine" in answer) or ("look" in answer):
            print(dedent("""
                  The room is dreary and unintersting. However, in the corner
                  lies a beautifully displayed treasure case.
                  """))

            return 'house_room'

        elif answer == 'stats':
            player.view_entity()

            return 'house_room'

        elif answer == 'attack':
            print(dedent("""
                  In a wild frenzy you pace around the house and attack the
                  various inanimate objects like a loon. Eventually you knock
                  into the trophy case, causing a vase on top to fall and break
                  upon your head.
                  """))

            return 'house_room'


        elif answer == 'check case':

            var = self.treasure_case.check_case()

            if var:
                return var

            elif not var:
                return 'house_room'

            else:
                raise Exception("ERROR HERE OWEN")

        elif answer == 'controls' or answer == 'help':
            print(dedent("""
                  On the far side of the wall, a blackboard is poorly pinned to
                  the crumbling wall. On it there are various scribbles, as
                  follows:
                  """))

            self.controls.view_controls()
            return 'house_room'

        else:
            print("\nSorry, I didn't quite get that.")

            return 'house_room'


class CollectTreasure(object):


    """
    This class is perhaps more of a function than a class, perhaps I could
    have made this into a module, or included it as a method in the TrollRoom
    class instead.
    """

    def activate(self, player, troll):

        print(dedent("""
              Congratulations, the troll is dead! Behind his corpse looms a
              shiny diamond. You pick it up and head south back to the house.
              After which, you add it to the Treasure Case.
              """))

        TreasureCase.treasure.append('Shiny diamond')

        return 'house_room'


class TrollRoom(object):

    """
    This is the room where the player fights the only enemy in the
    game. I've split this across the Troll Room and an Attack module. This is
    so in the future, I can add more enemies that have an attack sequence via
    the Attack module, rather than only the troll having it.
    """

    def __init__(self):
        """
        Used composition style again here. The TrollRoom class has-a Attack
        class
        """
        self.attack_sequence = Attack()

    def activate(self, player, troll):

        print(dedent("""
              You walk north through a pitch-black hole. Before you towers a
              massive troll like monster, teeth snarling and a mean-looking
              axe.
              """))

        answer2 = input("> ")

        if (answer2 == 'north' or answer2 == 'east') or (answer2 == 'west'):
            print(dedent("""
                  The troll blocks all of your escape routes, however, a quick move
                  south may save you."""))

            return 'troll_room'

        # Added a luck element here just to make it more intersting
        elif answer2 == 'south':
            luck = randint(1,2)

            if luck == 1:
                print(dedent("""
                      You decide to retreat, however the Troll has had his weat-a-bix
                      this morning and out steps you. Before you've even turned
                      around, the troll swings his axe and your head tumbles to
                      the floor.
                      """))

                return 'death_room'

            else:
                print(dedent("""
                      The troll seems to anticipate your intentions and cut off
                      your angle of retreat. Luckily, he slips on a
                      precariously placed banana skin, buying you precious
                      seconds to escape.
                      """))

                return 'house_room'

        # If I had coded the attack sequence here, I believe the TrollRoom
        # class would be too long, and decrease readability. Outsourcing it to
        # a different class (or in this case, a module) stops this issue.
        elif answer2 == 'attack':
            # The Attack module returns a result for us to use and it is
            # assigned to var, this is then returned back to the engine.
            var = self.attack_sequence.activate(player, troll)
            return var

        else:
            print("\nSorry, I didn't quite get that.")

            return 'troll_room'


class GalleryRoom(object):


    """
    This room is nice and simple and borderline lazy. The user must
    access this room first before attacking the troll, otherwise, the user
    dies.
    """

    def activate(self, player, troll):

        if player.inventory == {} and TreasureCase.treasure == []:
            # I have created this if-else statement so that the user can only
            # get the treasure and items once; without it a user could enter
            # this room twice andwin the game without facing the Troll.
            print(dedent("""
                  You discover one Golden Coin and a Silver Jewel Encrusted Crown.
                  Moreover, on the walls, you discover a sword and shield.
                  You decide to take everything, and return to the House.
                  """))
            # The use of random intergers means the attack_sequence will be
            # slighlty different every time, however, see the attack_module
            # file for a note on a bug.
            player.inventory['Sword'] = randrange(10, 41, 10)
            player.inventory['Shield'] = randrange(10, 41, 10)

            TreasureCase.treasure.append('Golden Coin')
            TreasureCase.treasure.append('Silver Jewel Encrused Crown')

            return 'house_room'

        else:
            print(dedent("""
                  You have already colleced the Sword, Shield, and two
                  treasures; there are no more items here for you.
                  """))

            return 'house_room'


class EndRoom(object):


    """ Quite simply ends the game once the user has won."""

    def activate(self, player, troll):
        print(dedent("""
              Congratulations! You won!
              """))
        exit(0)


class DeathRoom(object):


    """A classic death scene/room; very similiar to ex.43 version."""

    def activate(self, player, troll):

        death_quotes = [
            "You're dead. You're not very good at this, are you?",
            "You're dead. Honestly, what did you expect?",
            "You're dead. My 80 year old gran' can play better than this.",
            "You're dead. Not much of a surprise is it?",
            "You're dead. Surprise surprise...",
            "You're dead, bucko.",
            ]

        # A simpiier version of the ex43's version of choosing a random quote
        # from the list above; however one should take the time to understand
        # ex43's version.
        print(choice(death_quotes))

        exit(0)


class Map(object):

    """A simple Map that the engine uses to navigate through the script."""

    # Unsure of class is needed for such a simple bit of code.
    # The use of a dictionary here ensure that only one instance of each class
    # is stored. Some other ways kept producing new instances.
    rooms = {
        'house_room': HouseRoom(),
        'troll_room': TrollRoom(),
        'gallery_room': GalleryRoom(),
        'end_room': EndRoom(),
        'death_room': DeathRoom(),
        'collect_treasure': CollectTreasure(),
        }


class Engine(object):


    """
    The engine here is the driving force of the entire programme.
    It is based on ex43's design, however I believe it is slightly simplier
    """

    def __init__(self):
        """
        Once again I have used a composition format here. The engine has-a
        map of the game/script that it needs to run, it also has-a two entites
        that it needs to pass certain classess, in order for the attack
        sequence to work.
        """
        self.game_map = Map()
        self.player = CreateEntity()
        self.troll = CreateEntity()

    def run_engine(self):

        current_room = self.game_map.rooms.get('house_room')
        final_room = self.game_map.rooms.get('end_room')

        while current_room != final_room:
            next_room = current_room.activate(self.player, self.troll)
            current_room = self.game_map.rooms.get(next_room)

        current_room.activate(self.player, self.troll)


engine_obj = Engine()
engine_obj.run_engine()
