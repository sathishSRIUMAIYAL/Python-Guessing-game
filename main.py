import random

print('Welcome you all!')
number_of_players = input('To start the game, please press 5: ')
print("Guess the number from 1 to 5. The player who gets 3 points first is the winner!")

player1 = input("Player 1 - Please enter your name: ")
player2 = input("Player 2 - Please enter your name: ")

if number_of_players == '5':
    score_player1 = 0
    score_player2 = 0

    while score_player1 < 3 and score_player2 < 3:
        correct_number = random.randint(1, 5)

        try:
            player1_input = int(input(f"{player1}, guess a number (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if player1_input == correct_number:
            score_player1 += 1
            print(f"✅ {player1} guessed correctly!")
        else:
            print(f"❌ {player1} guessed wrong. The correct number was {correct_number}")

        correct_number = random.randint(1, 5)

        try:
            player2_input = int(input(f"{player2}, guess a number (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if player2_input == correct_number:
            score_player2 += 1
            print(f"✅ {player2} guessed correctly!")
        else:
            print(f"❌ {player2} guessed wrong. The correct number was {correct_number}")

        print("-" * 50)
        print(f"Scoreboard -> {player1}: {score_player1} | {player2}: {score_player2}")
        print("-" * 50)

    if score_player1 == 3:
        print(f"🎉🎊 {player1} wins the game!🏆🏅")
    else:
        print(f"🎉🎊 {player2} wins the game!🏆🏅")

else:
    print("Game not started. Please press 5 to begin.")
