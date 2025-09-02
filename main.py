import random
import tkinter as tk 

#command codes:
secret_number = random.randint(0,100)
repeats = 0
max_repeats = 10

def check_guess():
    global repeats
    guess = entry.get()

    if not guess.isdigit():
        label1.config(text="please enter a number!")
        return
    guess = int(guess)
    repeats += 1
    remaining_label.config(text=f"Remaining: {10-repeats}")
    guesses_box.config(state="normal")

    if guess == secret_number:
        label1.config(text=f"Bravo! the correct number is {secret_number}.")
        submit_button.config(state="disabled")
        guesses_box.insert(tk.END,f"{guess}","blue")
    elif repeats == max_repeats:
        label1.config(text=f"Game Over! the correct number is {secret_number}")
        submit_button.config(state="disabled")
    elif guess < secret_number:
        label1.config(text="The correct number is bigger.")
        guesses_box.insert(tk.END,f"{guess}, ","red")
    else:
        label1.config(text="The correct number is smaller.")
        guesses_box.insert(tk.END,f"{guess}, ","green")

    guesses_box.config(state="disabled")
    entry.delete(0, tk.END)

def game_restart():
    global secret_number, repeats
    secret_number = random.randint(0,100)
    repeats = 0
    label1.config(text="Game restarted!")
    guesses_box.config(state="normal") 
    guesses_box.delete("1.0", tk.END)   
    guesses_box.insert(tk.END, "Guesses: \n")
    guesses_box.config(state="disabled")
    submit_button.config(state="normal")
    remaining_label.config(text="Remaining: 10")
    entry.delete(0,tk.END)


#Graphic codes
game = tk.Tk()
game.config(bg="lightblue")
game.title("Guess Game")
game.geometry("400x300")

title_label = tk.Label(game, text="Guess a number between 0 and 100.", font=("Arial", 14), bg="lightblue")
title_label.pack()

entry = tk.Entry(game)
entry.pack(ipadx=30, pady=10)

submit_button = tk.Button(game, text="Guess!", command=check_guess, bg="lightgreen")
submit_button.pack(pady=10)

label1 = tk.Label(game, text="Hello, Welcome to Guess Game!", font=("Arial", 12), bg="lightblue")
label1.pack(pady=10)

remaining_label = tk.Label(game, text="Remaining: 10", font=("Arial",10), bg="lightblue", fg="red")
remaining_label.pack()

#guesses box
guesses_box = tk.Text(game, height=5, width=40, font=("Arial", 10))
guesses_box.pack()
guesses_box.tag_config("red", foreground="red")
guesses_box.tag_config("green", foreground="green")
guesses_box.tag_config("blue", foreground="blue")
guesses_box.insert(tk.END,"Guesses: \n")
guesses_box.config(state="disabled")

restart_button = tk.Button(game, text="Restart", command=game_restart, bg="lightyellow")
restart_button.pack()


game.mainloop()
