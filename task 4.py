import tkinter as tk
from tkinter import messagebox
import random
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"Computer chosen: {computer_choice}\nYOU chosen:{user_choice}\n{result}")
#photo reading
root = tk.Tk()
root.title("Rock-Paper-Scissors")
rock_photo = tk.PhotoImage(file="rock.gif")
paper_photo = tk.PhotoImage(file="paper.gif")
scissors_photo = tk.PhotoImage(file="scissors2.gif")

#creating grid
def create_button(image, command, row, column):
    canvas = tk.Canvas(root, width=500, height=700)
    canvas.grid(row=row, column=column, padx=20, pady=20)
    canvas.create_image(200,200, image=image)
    canvas.bind("<Button-1>", lambda event: command())

# Create buttons for user choices
create_button(rock_photo, lambda: play('Rock'), 0, 0)
create_button(paper_photo, lambda: play('Paper'), 0, 1)
create_button(scissors_photo, lambda: play('Scissors'), 0, 2)
root.mainloop()

