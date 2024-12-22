import random
import tkinter as tk
from tkinter import messagebox, simpledialog


def spooky_popup(title, message):
    """Display a spooky popup message."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    messagebox.showinfo(title, message)
    root.destroy()


def character_selection_gui():
    """GUI for selecting a character."""
    root = tk.Tk()
    root.title("Choose Your Character")

    selection = tk.StringVar(value="")

    def select_character():
        if selection.get():
            root.quit()

    characters = [
        "Police Officer: Calm under pressure, skilled with tactics.",
        "Scholar: Resourceful and puzzle-savvy.",
        "Athlete: Agile and strong, excels in physical challenges.",
        "Medic: Skilled at healing and resisting poison.",
        "Engineer: Master at disarming traps and fixing objects.",
        "Detective: Logical and observant, uncovers hidden clues.",
        "Magician: Deceptive and distracting.",
        "Survivalist: Endurance expert, resourceful in emergencies.",
        "Thief: Stealthy and adept at escaping unnoticed.",
        "Exorcist: Supernatural expert, banishes dark entities.",
    ]

    tk.Label(root, text="Choose Your Character", font=("Helvetica", 16)).pack(pady=10)

    for idx, char in enumerate(characters, 1):
        tk.Radiobutton(
            root, text=f"{idx}. {char}", variable=selection, value=char.split(":")[0], anchor="w", justify="left"
        ).pack(anchor="w", padx=20)

    tk.Button(root, text="Select", command=select_character).pack(pady=10)

    root.mainloop()
    return selection.get()


def random_death():
    """Random spooky death popup."""
    deaths = [
        "The shadows close in. You are lost forever.",
        "A horrifying scream fills the air. Everything goes black.",
        "The walls tremble, and you are crushed under the weight.",
        "A ghostly figure appears, and your life fades away.",
    ]
    spooky_popup("You Have Died", random.choice(deaths))


# Define door scenarios
def red_door(character):
    spooky_popup("The Red Door", "You open the red door and step into a fiery room. The walls seem to bleed molten heat.")
    choice = simpledialog.askinteger(
        "The Red Door",
        "What do you do?\n1. Manipulate a valve to flood the room with water.\n"
        "2. Use brute strength to break through a collapsing wall.\n"
        "3. Search for another way out."
    )

    if choice == 1:
        if character in ["Engineer", "Scholar", "Detective"]:
            spooky_popup("Success", "You expertly manipulate the valve, cooling the flames. You escape unharmed!")
            return "next"
        else:
            spooky_popup("Failure", "You fail to operate the valve. The fire consumes you.")
            return "death"
    elif choice == 2:
        if character in ["Athlete", "Survivalist"]:
            spooky_popup("Success", "Using your strength, you smash through the wall and escape!")
            return "next"
        else:
            spooky_popup("Failure", "You lack the strength. The flames consume you.")
            return "death"
    elif choice == 3:
        spooky_popup("Searching...", "You desperately search for another way out.")
        if random.random() > 0.5:
            spooky_popup("Success", "You find a hidden passage and escape!")
            return "next"
        else:
            spooky_popup("Failure", "You search in vain as the fire closes in. You perish.")
            return "death"
    else:
        spooky_popup("Indecision", "Indecision is fatal. The flames consume you.")
        return "death"


def green_door(character):
    spooky_popup("The Green Door", "You step into a lush jungle. Poisonous mist hangs heavily in the air.")
    choice = simpledialog.askinteger(
        "The Green Door",
        "What do you do?\n1. Hold your breath and run through.\n"
        "2. Use a makeshift filter to breathe.\n"
        "3. Search for an antidote."
    )

    if choice == 1:
        if character in ["Athlete", "Survivalist"]:
            spooky_popup("Success", "You hold your breath and make it through safely!")
            return "next"
        else:
            spooky_popup("Failure", "You can't hold your breath long enough. The poison overwhelms you.")
            return "death"
    elif choice == 2:
        if character in ["Engineer", "Medic"]:
            spooky_popup("Success", "You create a makeshift filter and breathe safely.")
            return "next"
        else:
            spooky_popup("Failure", "Your makeshift filter fails. The poison overtakes you.")
            return "death"
    elif choice == 3:
        if character in ["Scholar", "Detective"]:
            spooky_popup("Success", "You find an antidote and neutralize the poison!")
            return "next"
        else:
            spooky_popup("Failure", "You search in vain. The poison takes you.")
            return "death"
    else:
        spooky_popup("Indecision", "Indecision is fatal. The poison overtakes you.")
        return "death"


def final_door():
    spooky_popup("The Final Door", "You stand before the final, ominous door. Death awaits.")
    spooky_popup("Game Over", "As you open the door, darkness consumes you. There is no escape.")
    return "death"


def main():
    spooky_popup("Welcome", "Welcome to the Spooky Adventure!")
    character = character_selection_gui()
    if not character:
        spooky_popup("No Character Selected", "You must select a character to continue.")
        return
    spooky_popup("Character Selected", f"You chose: {character}. Prepare yourself!")

    door_options = ["Red Door", "Green Door"]
    while "Final Door" not in door_options:
        choice = simpledialog.askinteger(
            "Choose a Door",
            f"Available doors:\n1. {door_options[0]}\n2. {door_options[1]}\n"
            f"{'3. Final Door' if len(door_options) > 2 else ''}"
        )
        if choice == 1 and "Red Door" in door_options:
            result = red_door(character)
        elif choice == 2 and "Green Door" in door_options:
            result = green_door(character)
        elif choice == 3 and "Final Door" in door_options:
            result = final_door()
        else:
            spooky_popup("Invalid Choice", "Please choose a valid door.")
            continue

        if result == "death":
            return
        elif result == "next":
            door_options.pop(choice - 1)
            if not door_options:
                door_options.append("Final Door")

    final_door()


if __name__ == "__main__":
    main()
