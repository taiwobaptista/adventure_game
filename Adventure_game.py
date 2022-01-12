import time
import random


def print_pause(str):
    print(str)
    time.sleep(2)


def intro(creature):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def validate_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option not in options:
            print_pause("Please enter a valid input\n")
        else:
            return option


def cave(weapon, creature):
    if "magicalsword" in weapon:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("You walk back to the field.")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        weapon.append("magicalsword")
    field(weapon, creature)


def house(weapon, creature):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + creature + ".")
    print_pause(f"Eep! This is the {creature} s house!")
    print_pause(f"{creature} attacks you!")
    if "magicalsword" not in weapon:
        print_pause("\nYou feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        player_fight_or_run(weapon, creature)

    else:
        player_fight_or_run(weapon, creature)


def player_fight_or_run(weapon, creature):
    choice = validate_input(
        "Would you like to (1) fight or (2) run away?\n", ["1", "2"])
    if choice == "1":
        if "magicalsword" in weapon:
            print_pause(f"\nAs the  {creature} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the "
                        "attack.")
            print_pause(f"But the  {creature} one look at "
                        "your shiny new toy and runs away!")
            print_pause("\nYou have rid the town of the " + creature +
                        ". You are victorious!\n")
            play_again()
        else:
            print_pause("\nYou do your best...")
            print_pause(f"but your dagger is no match for the {creature}.")
            print_pause("You have been defeated!")
            play_again()

    elif choice == "2":
        print_pause("\nYou run back into the field. "
                    "\nLuckily, you don't seem to have been "
                    "followed.\n")
        field(weapon, creature)


def field(weapon, creature):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = validate_input("(Please enter 1 or 2.)\n", ["1", "2"])
        if choice1 == "1":
            house(weapon, creature)
            break
        elif choice1 == "2":
            cave(weapon, creature)
            break


def play_again():
    try_again = validate_input("Would you like to play again? (y/n)\n",
                               ["y", "n"])
    if try_again == "y":
        print_pause("\n\nExcellent! Restarting the game ...\n")
        play_game()
    elif try_again == "n":
        print_pause("Thanks for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    weapon = []
    creature = random.choice(["Dragon", "Comodo", "Pirate", "Troll"])
    intro(creature)
    field(weapon, creature)


if __name__ == "__main__":
    play_game()
