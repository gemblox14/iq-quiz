import tkinter as tk
from tkinter import messagebox
import random

# Extended list of IQ questions
questions = [
    {"question": "Which is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": "2"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Jupiter", "Earth", "Venus"], "answer": "Mars"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "answer": "Paris"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Gold", "Hydrogen"], "answer": "Oxygen"},
    {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Great White Shark", "Giraffe"], "answer": "Blue Whale"},
    {"question": "What is the chemical formula for water?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Korea", "Thailand"], "answer": "Japan"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": "Diamond"},
    {"question": "How many bones are in the adult human body?", "options": ["206", "208", "210", "215"], "answer": "206"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "answer": "Carbon Dioxide"},
    {"question": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
]

class IQGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IQ-Mas Game")
        self.geometry("400x300")
        self.configure(bg="#f0f8ff")  # Light blue background color

        self.start_screen()

    def start_screen(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()

        # Title label
        title_label = tk.Label(self, text="Welcome to IQ-Mas Game!", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
        title_label.pack(pady=20)

        self.question_count_label = tk.Label(self, text="Enter number of questions (1-100):", bg="#f0f8ff")
        self.question_count_label.pack(pady=10)

        self.question_count_entry = tk.Entry(self, font=("Helvetica", 12))
        self.question_count_entry.pack(pady=5)

        self.difficulty_label = tk.Label(self, text="Select Difficulty Level:", bg="#f0f8ff")
        self.difficulty_label.pack(pady=10)

        self.difficulty_var = tk.StringVar(value="Easy")

        easy_button = tk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="Easy", bg="#f0f8ff", font=("Helvetica", 12))
        easy_button.pack(anchor=tk.W)

        medium_button = tk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="Medium", bg="#f0f8ff", font=("Helvetica", 12))
        medium_button.pack(anchor=tk.W)

        hard_button = tk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="Hard", bg="#f0f8ff", font=("Helvetica", 12))
        hard_button.pack(anchor=tk.W)

        self.test_type_label = tk.Label(self, text="Select Test Type:", bg="#f0f8ff")
        self.test_type_label.pack(pady=10)

        self.test_type_var = tk.StringVar(value="IQ Test")

        iq_test_button = tk.Radiobutton(self, text="IQ Test", variable=self.test_type_var, value="IQ Test", bg="#f0f8ff", font=("Helvetica", 12))
        iq_test_button.pack(anchor=tk.W)

        reaction_test_button = tk.Radiobutton(self, text="Reaction Test", variable=self.test_type_var, value="Reaction Test", bg="#f0f8ff", font=("Helvetica", 12))
        reaction_test_button.pack(anchor=tk.W)

        start_button = tk.Button(self, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", font=("Helvetica", 14))
        start_button.pack(pady=20)

    def start_game(self):
        try:
            question_count = int(self.question_count_entry.get())
            if question_count < 1 or question_count > 100:
                raise ValueError("Invalid number of questions")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number between 1 and 100.")
            return

        self.difficulty = self.difficulty_var.get()
        self.test_type = self.test_type_var.get()
        self.remaining_questions = questions.copy()[:question_count]  # Select only the specified number of questions
        self.score = 0

        # Create a new window for the game
        self.game_window = tk.Toplevel(self)
        self.game_window.title("IQ Test Game")
        self.game_window.geometry("400x300")
        self.game_window.configure(bg="#f0f8ff")

        # Hide the start screen
        self.withdraw()

        # Setup game GUI components
        self.question_label = tk.Label(self.game_window, text="", font=("Helvetica", 14), wraplength=300, bg="#f0f8ff")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.game_window, text="", width=20, command=lambda i=i: self.check_answer(i), bg="#2196F3", fg="white", font=("Helvetica", 12))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.next_question()

    def next_question(self):
        if self.remaining_questions:
            q = random.choice(self.remaining_questions)
            self.remaining_questions.remove(q)  # Ensure questions are not repeated
            self.question_label.config(text=q["question"])

            # Randomize the order of options
            options = random.sample(q["options"], len(q["options"]))
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
        else:
            self.end_game()

    def check_answer(self, selected_index):
        selected_option = self.option_buttons[selected_index].cget("text")
        correct_answer = next(q["answer"] for q in questions if q["question"] == self.question_label.cget("text"))
        
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showerror("Wrong!", f"Oops, the correct answer was: {correct_answer}")

        self.next_question()

    def end_game(self):
        # Hide question and buttons, show final score
        self.question_label.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()

        final_score_label = tk.Label(self.game_window, text=f"Your final score: {self.score}/{len(questions)}", font=("Helvetica", 16), bg="#f0f8ff")
        final_score_label.pack(pady=20)

        # Show confetti if score is 5 or more
        if self.score >= 5:
            self.show_confetti()

        # Option to quit or restart
        restart_button = tk.Button(self.game_window, text="Play Again", command=self.restart_game, bg="#FFC107", fg="black", font=("Helvetica", 12))
        restart_button.pack(pady=10)
        quit_button = tk.Button(self.game_window, text="Quit", command=self.quit, bg="#F44336", fg="white", font=("Helvetica", 12))
        quit_button.pack(pady=10)

    def show_confetti(self):
        confetti_canvas = tk.Canvas(self.game_window, width=400, height=300, bg="#f0f8ff", highlightthickness=0)
        confetti_canvas.pack()

        # Generate random confetti
        for _ in range(100):
            x = random.randint(0, 400)
            y = random.randint(0, 300)
            color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
            confetti_canvas.create_oval(x, y, x + 5, y + 5, fill=color, outline=color)

    def restart_game(self):
        self.score = 0
        self.start_screen()  # Return to start screen

if __name__ == "__main__":
    game = IQGame()
    game.mainloop()
