# Productivity Tracker 9000
import time
import random

# Random phrases for when you just need a break
phrases = [
    "You're not as tired as you feel... maybe.",
    "Take a deep breath and sip some coffee. Or scream into a pillow.",
    "Every keystroke counts, even the wrong ones.",
    "Coding? Pffft, more like surviving.",
    "Press F to pay respects to your sanity."
]

def random_boost():
    """Prints a random phrase to keep you mildly entertained."""
    print("\n✨ Words of Wisdom ✨")
    print(random.choice(phrases))

def silly_task():
    """Simulates a random pointless task."""
    print("\n🤔 Doing a silly task...")
    time.sleep(2)
    print("Wow, that was pointless. But hey, you're still here.")

def main():
    print("Welcome to the Productivity Tracker 9000.")
    print("Pick your option below:\n")

    while True:
        print("1. Get some words of wisdom")
        print("2. Waste time with a silly task")
        print("3. Escape this chaos\n")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            random_boost()
        elif choice == "2":
            silly_task()
        elif choice == "3":
            print("\nTake care out there. You're doing fine. ✌️")
            break
        else:
            print("Oops, not a valid choice. Try again if you care.")

# Run the tracker
if __name__ == "__main__":
    main()
