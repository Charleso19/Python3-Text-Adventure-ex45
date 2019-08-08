from textwrap import dedent
from random import choice, randrange, randint
from math import sqrt

"""This module consists of the single class below"""

# So far I have found one bug in the code, sometimes when attacking either the
# Troll's or Player's hp is not affected. I believe this is because the maths
# I have used is flawed.

class Attack(object):


    """
    This class is responsible for the entire attack sequence of the game.
    I decided to turn it into a module, rather than keep it in the original
    script, in order to maximise readability.
    """

    def activate(self, player, troll):
        """This is the only method in the class, it simply initiates or
        'activates' the attack sequence.
        """

        if player.inventory == {}:
            print(dedent("""
                  Your inventory is empty. You have nothing to defend yourself
                  with or attack with. The troll, although a dumb-looking thing,
                  notices how unprepared you are.
                  He swings his axe and slices you in half.
                  """))

            return 'death_room'

        # I could maybe have used an else statement here instead of this long
        # elif statement, however, it does make clear that the sword and shield
        # are needed to progress (to the programmer that is, not necessarily
        # the user playing the game!).
        elif 'Sword' in player.inventory and 'Shield' in player.inventory:

            player.attack += player.inventory.get('Sword')
            player.defence += player.inventory.get('Shield')

            # I wanted to ensure zero was never an option, and after playing
            # with randrange and randint, the two while loops below were the
            # simpliest option I could figure out
            # However, I should have probably included these two manipulations
            # of the Troll's stats in the entity_module module, rather than here.
            while True:

                rand = randrange(0, 31, 10)

                if rand == 0:
                    pass
                else:
                    break

            while True:

                rand2 = randrange(0, 31, 10)

                if rand2 == 0:
                    pass
                else:
                    break

            troll.attack += rand
            troll.defence += rand2

            print(dedent("""
                  You unsheath your sword and don your shield. The troll grips
                  tightly his axe; a sheet of sweat glistens on his gigantic
                  forehead.
                  """))

            troll_alive = True
            player_alive = True

            while troll_alive and player_alive:

                answer3 = input("Press ENTER to attack! ")

                chance = randint(1,2)

                if chance == 1:
                    print(dedent("""
                          STRIKE!! You hurt the Troll!!
                          """))


                    troll.hp = int(troll.hp - sqrt((troll.defence - player.attack)**2))
                    print(f"Troll's hp: {troll.hp}")

                    if troll.hp <= 0:
                        print("THE TROLL IS DEAD!")
                        troll_alive = False

                        return 'collect_treasure'

                    else:
                        continue

                else:
                    types_of_troll_attack = [
                        "The troll dodges your swipe and clocks you with the handle of his axe.",
                        "*SWOOSH* the troll slices down your chest; a stream of blood shows.",
                        "The troll strikes you with his axe!",
                        "The axe slashes at your body.",
                        "The troll commits a thunderous blow to your head!",
                        "The troll slices you!",
                        ]

                    print(choice(types_of_troll_attack))

                    player.hp = int(player.hp - sqrt((player.defence - troll.attack)**2))
                    print(f"Player's hp: {player.hp}")

                    if player.hp <= 0:
                        print("With a final fatal blow, the troll has sliced you in half.")
                        player_alive = False
                        return 'death_room'






        else:
            raise Exception("ERROR HERE OWEN")
