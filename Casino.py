import random
import os

Money = 1000


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    global Money
    clear_screen()
    print("Welcome to Secret Casino ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("       Have Fun           ")
    print()
    print(f'Balance: {Money}')
    print()
    print("1: Dice")
    print("2: Roulette")
    print("3: BlackJack")

    while True:
        try:
            options = float(input("Choose a game (1, 2, 3): "))
            if options not in (1.0, 2.0, 3.0):
                print("Choose a valid number (1.0, 2.0, or 3.0)")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if options == 1.0:
        dice_game()
    elif options == 2.0:
        roulette_game()
    elif options == 3.0:
        blackjack_game()


def display_dice(face):
    dice_faces = {
        1: """
        +-----+
        |     |
        |  o  |
        |     |
        +-----+
        """,
        2: """
        +-----+
        | o   |
        |     |
        |   o |
        +-----+
        """,
        3: """
        +-----+
        | o   |
        |  o  |
        |   o |
        +-----+
        """,
        4: """
        +-----+
        | o o |
        |     |
        | o o |
        +-----+
        """,
        5: """
        +-----+
        | o o |
        |  o  |
        | o o |
        +-----+
        """,
        6: """
        +-----+
        | o o |
        | o o |
        | o o |
        +-----+
        """
    }
    print(dice_faces[face])


def roll_dice():
    roll = random.randint(1, 6)
    display_dice(roll)
    return roll


def dice_game():
    global Money
    clear_screen()
    print("Welcome to the Dice game!")
    print("$$$$$$$$$$$$$$$")
    print("If you roll a 1, 2, or 3, you win and double your bet. If you roll a 4, 5, or 6, you lose your bet.")
    print()

    while True:
        try:
            Bet = float(input(f"Your Bet (Current Balance: {Money}): "))
            if Bet > Money:
                print("Not enough Money!")
                continue
            elif Bet <= 0:
                print("Bet must be greater than 0!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("Rolling the dice...")
    roll = roll_dice()

    if roll in [1, 2, 3]:
        print(f"You rolled {roll} and won {Bet * 2}!")
        Money += Bet
    elif roll in [4, 5, 6]:
        print(f"You rolled {roll} and lost {Bet}.")
        Money -= Bet

    print(f"Your new balance is: {Money}")
    play_again()


def play_again():
    global Money
    while True:
        play_choice = input("Do you want to play again? (y/n): ").lower()
        if play_choice == 'y':
            main()
            break
        elif play_choice == 'n':
            main()
            break
        else:
            print("Invalid choice! Please type 'y' or 'n'.")


def roulette_game():
    global Money
    clear_screen()
    print("Welcome to Roulette!")
    print("$$$$$$$$$$$$$$$")
    print("Place your bet on a number between 0 and 36, or choose 'even' or 'odd'.")
    print()

    while True:
        try:
            Bet = float(input(f"Your Bet (Current Balance: {Money}): "))
            if Bet > Money:
                print("Not enough Money!")
                continue
            elif Bet <= 0:
                print("Bet must be greater than 0!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    bet_type = input("Do you want to bet on a specific number (0-36) or 'even'/'odd': ").lower()
    if bet_type == "even" or bet_type == "odd":
        roulette_result = random.randint(0, 36)
        print(f"------------")
        print(f"|   {roulette_result}   |")
        print(f"------------")
        print(f"The roulette wheel landed on {roulette_result}.")

        if bet_type == "even" and roulette_result % 2 == 0:
            print(f"You won {Bet * 2}!")
            Money += Bet
        elif bet_type == "odd" and roulette_result % 2 != 0:
            print(f"You won {Bet * 2}!")
            Money += Bet
        else:
            print(f"You lost {Bet}.")
            Money -= Bet
    else:
        try:
            bet_number = int(bet_type)
            if bet_number < 0 or bet_number > 36:
                print("Invalid number! Please enter a number between 0 and 36.")
                return
            roulette_result = random.randint(0, 36)
            print(f"------------")
            print(f"|   {roulette_result}   |")
            print(f"------------")
            print(f"The roulette wheel landed on {roulette_result}.")

            if bet_number == roulette_result:
                print(f"You won {Bet * 35}!")
                Money += Bet * 35
            else:
                print(f"You lost {Bet}.")
                Money -= Bet
        except ValueError:
            print("Invalid input! Please enter a valid number or 'even'/'odd'.")
            return

    print(f"Your new balance is: {Money}")
    play_again()


def blackjack_game():
    global Money
    clear_screen()
    print("Welcome to Blackjack!")
    print("$$$$$$$$$$$$$$$")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards are worth 10, Aces are worth 1 or 11.")
    print()

    while True:
        try:
            Bet = float(input(f"Your Bet (Current Balance: {Money}): "))
            if Bet > Money:
                print("Not enough Money!")
                continue
            elif Bet <= 0:
                print("Bet must be greater than 0!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def calculate_hand(hand):
        total = 0
        ace_count = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                ace_count += 1
                total += 11
            else:
                total += int(card)
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1
        return total

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Your hand: {player_hand}, total: {calculate_hand(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]} and a hidden card.")

    while calculate_hand(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            print(f"Your hand: {player_hand}, total: {calculate_hand(player_hand)}")
        elif action == 'stand':
            break

    player_total = calculate_hand(player_hand)
    if player_total > 21:
        print(f"You went over 21! Your total: {player_total}")
        Money -= Bet
        print(f"Your new balance is: {Money}")
        play_again()

    print(f"Dealer's hand: {dealer_hand}, total: {calculate_hand(dealer_hand)}")
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print(f"Dealer's hand: {dealer_hand}, total: {calculate_hand(dealer_hand)}")

    dealer_total = calculate_hand(dealer_hand)
    if dealer_total > 21 or player_total > dealer_total:
        print(f"You win {Bet}!")
        Money += Bet
    elif player_total < dealer_total:
        print(f"You lose {Bet}.")
        Money -= Bet
    else:
        print("It's a tie!")

    print(f"Your new balance is: {Money}")
    play_again()


main()
