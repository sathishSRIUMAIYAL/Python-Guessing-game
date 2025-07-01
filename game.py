import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x400")

        self.score_player1 = 0
        self.score_player2 = 0
        self.round = 1

        self.start_screen()

    def start_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Welcome to the Number Guessing Game", font=('Arial', 14)).pack(pady=10)
        tk.Label(self.root, text="Enter 5 to Start the Game").pack()

        self.start_entry = tk.Entry(self.root)
        self.start_entry.pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.validate_start).pack(pady=10)

    def validate_start(self):
        if self.start_entry.get() == '5':
            self.get_player_names()
        else:
            messagebox.showerror("Error", "Please enter 5 to start the game!")

    def get_player_names(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Player Names", font=('Arial', 14)).pack(pady=10)

        tk.Label(self.root, text="Player 1 Name:").pack()
        self.player1_name = tk.Entry(self.root)
        self.player1_name.pack(pady=5)

        tk.Label(self.root, text="Player 2 Name:").pack()
        self.player2_name = tk.Entry(self.root)
        self.player2_name.pack(pady=5)

        tk.Button(self.root, text="Continue", command=self.start_game).pack(pady=10)

    def start_game(self):
        self.player1 = self.player1_name.get()
        self.player2 = self.player2_name.get()

        if not self.player1 or not self.player2:
            messagebox.showerror("Error", "Please enter both names!")
            return

        self.play_round()

    def play_round(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Round {self.round}", font=('Arial', 14)).pack(pady=5)
        tk.Label(self.root, text=f"{self.player1}, guess a number between 1-5").pack()
        self.p1_input = tk.Entry(self.root)
        self.p1_input.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.check_player1).pack(pady=5)

    def check_player1(self):
        try:
            guess = int(self.p1_input.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a number!")
            return

        correct = random.randint(1, 5)
        if guess == correct:
            self.score_player1 += 1
            messagebox.showinfo("Result", f"✅ {self.player1} guessed correctly!")
        else:
            messagebox.showinfo("Result", f"❌ {self.player1} guessed wrong. It was {correct}")

        self.check_player2()

    def check_player2(self):
        self.clear_screen()

        tk.Label(self.root, text=f"{self.player2}, guess a number between 1-5").pack()
        self.p2_input = tk.Entry(self.root)
        self.p2_input.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.check_player2_result).pack(pady=5)

    def check_player2_result(self):
        try:
            guess = int(self.p2_input.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a number!")
            return

        correct = random.randint(1, 5)
        if guess == correct:
            self.score_player2 += 1
            messagebox.showinfo("Result", f"✅ {self.player2} guessed correctly!")
        else:
            messagebox.showinfo("Result", f"❌ {self.player2} guessed wrong. It was {correct}")

        self.show_scores()

    def show_scores(self):
        if self.score_player1 == 3:
            self.show_winner(self.player1)
        elif self.score_player2 == 3:
            self.show_winner(self.player2)
        else:
            self.round += 1
            self.play_round()

    def show_winner(self, winner):
        self.clear_screen()
        tk.Label(self.root, text=f"🎉 Congratulations {winner}! 🎉", font=('Arial', 16), fg='green').pack(pady=20)
        tk.Label(self.root, text=f"{self.player1} Score: {self.score_player1}", font=('Arial', 12)).pack(pady=5)
        tk.Label(self.root, text=f"{self.player2} Score: {self.score_player2}", font=('Arial', 12)).pack(pady=5)
        tk.Button(self.root, text="Play Again", command=self.reset_game).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def reset_game(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.round = 1
        self.start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
root = tk.Tk()
app = GuessingGame(root)
root.mainloop()
