import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x200")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        # Label and Entry for user input
        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Button to submit guess
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)
        
        # Label to show result or hint
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
        
        # Button to restart the game
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state="disabled")
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.")
                self.guess_button.config(state="disabled")
                self.restart_button.config(state="normal")
                messagebox.showinfo("Congratulations", f"You guessed the number {self.target_number} in {self.attempts} attempts!")
        
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            
    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.guess_button.config(state="normal")
        self.restart_button.config(state="disabled")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
