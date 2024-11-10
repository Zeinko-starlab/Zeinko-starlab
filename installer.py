import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Program code stored in separate variables
program_one_code = """import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Computer randomly selects a number
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
"""

program_two_code = """import random

def rock_paper_scissors(username):
    print("Welcome to Rock, Paper, Scissors!")
    
    if username == 'Zeinko':
        print("Easy mode activated!")

    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if player_choice == 'exit':
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Computer makes a choice (easy mode: always chooses rock)
        if username == 'Zeinko':
            computer_choice = "rock"
        else:
            computer_choice = random.choice(choices)
        
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors('Zeinko')
"""

program_three_code = """import random

def hangman(username):
    words = ["python", "hangman", "game", "computer", "programming"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts_left > 0:
        # Display current state of the word with guessed letters
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
        print(f"Word to guess: {display_word}")

        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print(f"Incorrect guess! You have {attempts_left} attempts left.")
        else:
            print("Good guess!")

    if attempts_left == 0:
        print(f"Game over! The word was: {word_to_guess}")

hangman('Zeinko')
"""

# Placeholder program code variables
new_program_code_1 = """def sort_list(numbers, order):
    # Sort the list in ascending or descending order based on user choice.
    if order == "1":
        return sorted(numbers)
    elif order == "2":
        return sorted(numbers, reverse=True)
    else:
        print(translate("Invalid choice, please enter 1 or 2."))
        return None

def translate(text, lang="en"):
    # Translate English text to French or Arabic.
    translations = {
        "en": {
            "Enter a list of numbers separated by commas": "Enter a list of numbers separated by commas",
            "Choose sorting order:\n1. Ascending\n2. Descending": "Choose sorting order:\n1. Ascending\n2. Descending",
            "The sorted list is": "The sorted list is",
            "Invalid choice, please enter 1 or 2.": "Invalid choice, please enter 1 or 2.",
            "Invalid input, please enter numbers only.": "Invalid input, please enter numbers only."
        },
        "fr": {
            "Enter a list of numbers separated by commas": "Entrez une liste de nombres séparés par des virgules",
            "Choose sorting order:\n1. Ascending\n2. Descending": "Choisissez l'ordre de tri :\n1. Croissant\n2. Décroissant",
            "The sorted list is": "La liste triée est",
            "Invalid choice, please enter 1 or 2.": "Choix invalide, veuillez entrer 1 ou 2.",
            "Invalid input, please enter numbers only.": "Entrée invalide, veuillez entrer uniquement des nombres."
        },
        "ar": {
            "Enter a list of numbers separated by commas": "أدخل قائمة الأرقام مفصولة بفواصل",
            "Choose sorting order:\n1. Ascending\n2. Descending": "اختر ترتيب الفرز:\n1. تصاعدي\n2. تنازلي",
            "The sorted list is": "القائمة المرتبة هي",
            "Invalid choice, please enter 1 or 2.": "خيار غير صالح، يرجى إدخال 1 أو 2.",
            "Invalid input, please enter numbers only.": "إدخال غير صالح، يرجى إدخال الأرقام فقط."
        }
    }
    return translations.get(lang, {}).get(text, text)

def main():
    # Choose language
    lang = input("Choose language (en/fr/ar): ").lower()
    if lang not in ["en", "fr", "ar"]:
        print("Invalid language, defaulting to English.")
        lang = "en"

    # Get input list from user
    try:
        numbers = list(map(int, input(translate("Enter a list of numbers separated by commas", lang) + ": ").split(',')))
    except ValueError:
        print(translate("Invalid input, please enter numbers only.", lang))
        return
    
    # Get sorting order from user
    order = input(translate("Choose sorting order:\n1. Ascending\n2. Descending", lang) + ": ")
    sorted_numbers = sort_list(numbers, order)
    
    if sorted_numbers is not None:
        print(f"{translate('The sorted list is', lang)}: {sorted_numbers}")

# Run the program
main()"""
new_program_code_2 = """import random
import time
import os

def clear_console():
	os.system("clear")

questions = [
    "If Aria were 9, and Sara is double her age, what would be the total of their ages combined?",
    "If a ball traveled 7 m/s, how long would it take to travel 35m + 7km in seconds?",
    "What is the most common function name if the comment was written as # Adds money to the player"
]
answers = ["their total age is 27", "1005 seconds", "add_money"]

money = 0  # Initial money
wait_time = 2.5  # Initial wait time
coins = 0  # Initial coins
premium = False # Set this to True if the user has premium; False otherwise
bought = False
jackpot_chance = 0  # Base jackpot chance
boosters = 0  # Number of boosters available
boost_time = 0  # Time until the booster effect expires
active_boosters = 0  # Number of boosters currently used
used_boosters = active_boosters  # Number of all boosters used
total_money = 0  # All money 
total_coins = 0  # All coins



def legit_use_booster():
    global boosters, jackpot_chance, boost_time, active_boosters

    if boosters > 0:
        print("You have", boosters, "boosters available.")
        print("1. Use 1 booster (15 seconds)")
        print("2. Use 2 boosters (30 seconds)")
        print("3. Use 3 boosters (45 seconds)")
        choice = input("Choose an option by number (1, 2, 3): ")

        if choice == "1" and boosters >= 1:
            boosters -= 1
            active_boosters = 1
            boost_time = time.time() + 15  # 15 seconds
            jackpot_chance += 5
            print("1 booster used! Jackpot chance increased by 5% for 15 seconds.")
        elif choice == "2" and boosters >= 2:
            boosters -= 2
            active_boosters = 2
            boost_time = time.time() + 30  # 30 seconds
            jackpot_chance += 10  # 5% * 2
            print("2 boosters used! Jackpot chance increased by 10% for 30 seconds.")
        elif choice == "3" and boosters >= 3:
            boosters -= 3
            active_boosters = 3
            boost_time = time.time() + 45  # 45 seconds
            jackpot_chance += 15  # 5% * 3
            print("3 boosters used! Jackpot chance increased by 15% for 45 seconds.")
        else:
            print("Not enough boosters or invalid choice.")
    else:
        print("No boosters left.")




def conversion():
    global money, coins, total_coins
    print("1. Convert money to coins.")
    print("2. Convert coins to money.")
    choice = input("1 or 2: ")
    if choice == "1":
        if money < 1:
            print("nuh uh, I ain't getting scammed today")
        else:
            coins += money / 10
            total_coins += money / 10
            money = 0
            print("Exchanged!")
    elif choice == "2":
        if coins < 1:
            print("nuh uh")
        else:
            money += coins * 10
            total_money += coins * 10
            coins = 0
            print("Exchanged!")

def stats():
    global money, coins, total_money
    print(f"Current money: {money}")
    print(f"Current coins: {coins}")
    print(f"Total money: {total_money}")
    print(f"Total coins: {total_coins}")

def upgrade_menu():
    global coins, money, wait_time, premium
    print("1. Double Money (1 coin)")
    print("2. Gain $5 (0.5 coins)")
    print("3. Buy Premium (20 coins)")
    print("4. Reduce roll wait time (4 coins)")
    choice = input("Choose an option by number: ")
    if choice == "1":
        if coins >= 1:
            coins -= 1
            money *= 2
            print("Doubled your money!")
        else:
            print("Insufficient coins!")
    elif choice == "2":
        if coins >= 0.5:
            coins -= 0.5
            money += 5
            total_money += 5
            print("Gained $5!")
        else:
            print("Insufficient coins!")
    elif choice == "3":
        if not premium and coins >= 20:
            coins -= 20
            premium = True
            print("Premium purchased!")
        else:
            print("Already have premium or insufficient coins!")
    elif choice == "4":
        if coins >= 4:
            coins -= 4
            wait_time = max(1, wait_time - 1)
            print("Reduced wait time for rolling!")
        else:
            print("Insufficient coins!")

def mod_menu(name, passw):
    global jackpot_chance, boosters, premium
    username = "Zeinko"
    password = "Omar123???"

    if name == username and passw == password:
        print("Access granted to mod menu!")
        print("1. Change Money.")
        print("2. Change Coins.")
        print("3. Toggle Premium.")
        print("4. Change Questions.")
        print("5. Change Answers.")
        print("6. Change Wait time.")
        print("7. Increase Jackpot Chance.")
        print("8. Use Jackpot Boosters.")
        print("9. Spawn Boosters.")
        choice = input("Choose an option: ")

        if choice == "1":
            new_value = input("New Money: ")
            try:
                money = int(new_value)
                total_money += money
                print("Money Changed!")
            except ValueError:
                print("Invalid input for money.")
        elif choice == "2":
            new_value = input("New Coins: ")
            try:
                coins = int(new_value)
                total_coins += coins
                print("Coins Changed!")
            except ValueError:
                print("Invalid input for coins.")
        elif choice == "3":
            premium = not premium
            print(f"Premium set to {premium}.")
        elif choice == "4":
            questions.clear()
            new_questions = input("Enter new questions separated by commas: ").split(',')
            questions.extend(new_questions)
            print("Questions updated.")
        elif choice == "5":
            answers.clear()
            new_answers = input("Enter new answers separated by commas: ").split(',')
            answers.extend(new_answers)
            print("Answers updated.")
        elif choice == "6":
            new_wait = input("Enter new wait time: ")
            try:
                wait_time = float(new_wait)
                print("Wait time updated.")
            except ValueError:
                print("Invalid input for wait time.")
        elif choice == "7":
            increase_chance = input("Increase Jackpot chance by how much? ")
            try:
                jackpot_chance += int(increase_chance)
                print(f"Jackpot chance increased. New chance: {jackpot_chance}%")
            except ValueError:
                print("Invalid input for jackpot chance.")
        elif choice == "8":
            use_booster()
        elif choice == "9":
            spawn_boosters()

def use_booster():
    global boosters, jackpot_chance, boost_time, active_boosters
    if boosters > 0:
        print(f"You have {boosters} boosters.")
        choice = input("Use how many boosters (1-3): ")
        try:
            boost_count = int(choice)
            if 1 <= boost_count <= min(3, boosters):
                boosters -= boost_count
                active_boosters = boost_count
                boost_time = time.time() + (boost_count * 15)
                jackpot_chance += boost_count * 5
                print(f"Used {boost_count} boosters. Jackpot chance increased by {boost_count * 5}%")
            else:
                print("Invalid booster amount.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No boosters left.")

def spawn_boosters():
    global boosters
    boosters += 3
    print("3 boosters spawned.")

def buy_boosters():
    global coins, boosters
    booster_price = 5
    if coins >= booster_price:
        booster_count = coins // booster_price
        boosters += booster_count
        coins -= booster_count * booster_price
        print(f"Bought {booster_count} boosters.")
    else:
        print("Not enough coins.")

def roll():
    global money, jackpot_chance, total_money
    input("Press enter to roll: ")
    jackpot_roll = random.randint(0, 10000)
    roll_value = random.randint(1, 9)
    boosted_roll = random.randint(20, 40)
    money += roll_value
    total_money += roll_value
    time.sleep(wait_time)
    if random.randint(0, 10) == 0:
    	money += boosted_roll + roll_value
    	print(f"1/10 Chance Achieved! Money: {money}$")

    if time.time() > boost_time:
        active_boosters = 0
        jackpot_chance = max(jackpot_chance - 5 * active_boosters, 0)

    if jackpot_roll < jackpot_chance:
        money += 777
        total_money += 777
        print("JACKPOT!!!!!!!!! +777 MONEY!!!!!")
    else:
        print(f"Rolled! You gained ${roll_value}. Total money: ${money}")

def main_shop():
    print("1. Buy Boosters")
    print("2. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        buy_boosters()
    elif choice == "2":
        print("Exiting shop.")

def main():
    print("1. Roll")
    print("2. Mod Menu")
    print("3. Shop")
    print("4. Upgrades")
    print("5. Conversion")
    print("6. Stats")
    print("7. Use Boosters")
    choice = input("Choose an option: ")

    if choice == "1":
        roll()
    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        mod_menu(username, password)
    elif choice == "3":
        main_shop()
    elif choice == "4":
        upgrade_menu()
    elif choice == "5":
        conversion()
    elif choice == "6":
        stats()
    elif choice == "7":
    	legit_use_booster()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(2)
        clear_console()"""
new_program_code_3 = """# Placeholder for New Program 3"""
new_program_code_4 = """# Placeholder for New Program 4"""
new_program_code_5 = """# Placeholder for New Program 5"""
new_program_code_6 = """# Placeholder for New Program 6"""
new_program_code_7 = """# Placeholder for New Program 7"""
new_program_code_8 = """# Placeholder for New Program 8"""
new_program_code_9 = """# Placeholder for New Program 9"""
new_program_code_10 = """# Placeholder for New Program 10"""
new_program_code_11 = """# Placeholder for New Program 11"""
new_program_code_12 = """# Placeholder for New Program 12"""
new_program_code_13 = """# Placeholder for New Program 13"""

# Predefined list of programs, each with a key
programs = {
    "RNG": {
        "file_name": "number_guessing.py",
        "code": program_one_code
    },
    "RPS": {
        "file_name": "RockPaperScissors.py",
        "code": program_two_code
    },
    "HM": {
        "file_name": "Hangman.py",
        "code": program_three_code
    },
    "LS": {
        "file_name": "ListSorter.py",
        "code": new_program_code_1
    },
    "NG": {
        "file_name": "NewGame.py",
        "code": new_program_code_2
    },
    "NEW3": {
        "file_name": "NewProgram3.py",
        "code": new_program_code_3
    },
    "NEW4": {
        "file_name": "NewProgram4.py",
        "code": new_program_code_4
    },
    "NEW5": {
        "file_name": "NewProgram5.py",
        "code": new_program_code_5
    },
    "NEW6": {
        "file_name": "NewProgram6.py",
        "code": new_program_code_6
    },
    "NEW7": {
        "file_name": "NewProgram7.py",
        "code": new_program_code_7
    },
    "NEW8": {
        "file_name": "NewProgram8.py",
        "code": new_program_code_8
    },
    "NEW9": {
        "file_name": "NewProgram9.py",
        "code": new_program_code_9
    },
    "NEW10": {
        "file_name": "NewProgram10.py",
        "code": new_program_code_10
    },
    "NEW11": {
        "file_name": "NewProgram11.py",
        "code": new_program_code_11
    },
    "NEW12": {
        "file_name": "NewProgram12.py",
        "code": new_program_code_12
    },
    "NEW13": {
        "file_name": "NewProgram13.py",
        "code": new_program_code_13 # These are placeholders if you want to change them, change them.
    }
}

def write_code_to_file(file_name, program_code):
    """Writes the given code to a new Python file."""
    with open(file_name, 'w') as file:
        file.write(program_code)
    print(f"Code written to {file_name}")

def run_and_cleanup(file_name):
    """Runs the created Python file and deletes the installer script."""
    subprocess.run(["python", file_name])

def select_directory(label_path_var):
    """Opens a file dialog to let the user select a folder and update the label."""
    folder_path = filedialog.askdirectory(title="Choose where to save the file")
    if folder_path:
        label_path_var.set(f"Selected path: {folder_path}")
    return folder_path

def validate_key(key):
    """Check if the entered key matches any program's key."""
    if key in programs:
        return programs[key]["file_name"], programs[key]["code"]
    return None, None

def create_gui():
    """Creates and runs the GUI for entering the key and installing the program."""
    root = tk.Tk()
    root.title("Program Installer (Dark Mode)")

    # Set dark mode background and text colors
    root.configure(bg="#2e2e2e")
    root.geometry("400x300")

    label = tk.Label(root, text="Enter the key to install a program:", bg="#2e2e2e", fg="white", font=("Times New Roman", 11))
    label.pack(pady=20)

    key_entry = tk.Entry(root, bg="#4e4e4e", fg="white", font=("Times New Roman", 12))
    key_entry.pack(pady=10)

    # Label for showing the chosen directory
    label_path_var = tk.StringVar()
    label_path = tk.Label(root, text="No path selected", bg="#2e2e2e", fg="white", font=("Times New Roman", 10))
    label_path.pack(pady=10)

    def on_key_entered(event=None):
        """Handle the key validation and program installation."""
        entered_key = key_entry.get()
        program_file, program_code = validate_key(entered_key)
        
        if program_file:
            # If the key matches, prompt user for directory and save the program
            folder_path = select_directory(label_path_var)
            if folder_path:
                new_file_name = os.path.join(folder_path, program_file)
                write_code_to_file(new_file_name, program_code)

                # Run the file and clean up the installer
                run_and_cleanup(new_file_name)
                root.quit()
        else:
            print("Invalid key entered. Please try again.")
    
    # Bind the Enter key to trigger the program installation
    key_entry.bind("<Return>", on_key_entered)

    # Button to open the file dialog
    choose_path_button = tk.Button(root, text="Choose Save Path", bg="#4e4e4e", fg="white", font=("Times New Roman", 12), command=lambda: select_directory(label_path_var))
    choose_path_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()