import tkinter as tk
import random

# MAIN SCREEN
root = tk.Tk()
root.title("Game")
root.configure(bg="hot pink")
root.geometry("800x600")
root.resizable(False, False)

# VARIABLES
num = tk.IntVar()
round = 0

# ROCK PAPER SCISSOR CLICK FUNCTION
def click_rps(idx):
    global Design_instance
    result_text = ""
    result_color = "white"
    ai_choose = random.choice(["ROCK", "PAPER", "SCISSOR"])

    if hasattr(Design_instance, "result_label") and Design_instance.result_label:
        Design_instance.result_label.destroy()

    if idx == "BACK":
        Design_instance.reset_main_design()
        Design_instance.f5.destroy()
        Design_instance = Design(root)
        root.configure(bg="hot pink")
    else:
        if idx == ai_choose:
            result_text = f"AI CHOOSED: {ai_choose} You Choose: {idx} -----> DRAW"
            result_color = "white"
        elif idx == "ROCK" and ai_choose == "PAPER" or \
                idx == "PAPER" and ai_choose == "SCISSOR" or \
                idx == "SCISSOR" and ai_choose == "ROCK":
            result_text = f"AI CHOOSED: {ai_choose} You Choose: {idx} -----> AI WIN"
            result_color = "red"
        else:
            result_text = f"AI CHOOSED: {ai_choose} You Choose: {idx} -----> YOU WIN"
            result_color = "green"

        Design_instance.result_label = tk.Label(
            Design_instance.f5,
            text=result_text,
            font=("Arial", 20, "bold"),
            bg="black",
            fg=result_color
        )
        Design_instance.result_label.pack(pady=10)

# ROCK PAPER SCISSOR FUNCTION
def rps():
    Design_instance.reset_main_design()
    root.configure(bg="black")
    Design_instance.f5.config(bg="black")
    for i, option in enumerate(["ROCK", "PAPER", "SCISSOR", "BACK"]):
        button = tk.Button(
            Design_instance.f5,
            text=option,
            font=("Arial", 20, "bold"),
            bg="black",
            fg="hot pink",
            borderwidth=0,
            command=lambda idx=option: click_rps(idx)
        )
        button.pack(pady=1)

# GUESS THE NUMBER FUNCTION CLICK FUNCTION
def click_gtn(idx):
    global Design_instance, ai_choice, round
    result_text = ""
    result_color = "white"
    if hasattr(Design_instance, "result_label") and Design_instance.result_label:
        Design_instance.result_label.destroy()

    if idx == "BACK":
        Design_instance.reset_main_design()
        Design_instance.f5.destroy()
        Design_instance = Design(root)
        root.configure(bg="hot pink")
    else:
        if idx == "SUBMIT":
            if round <= 8:
                user_choice = num.get()
                if user_choice < ai_choice:
                    round += 1
                    result_text = f"You Choose: {user_choice} -----> LOW | Chance Left: {10 - round}"
                    result_color = "orange"
                elif user_choice > ai_choice:
                    round += 1
                    result_text = f"You Choose: {user_choice} -----> HIGH | Chance Left: {10 - round}"
                    result_color = "red"
                else:
                    result_text = f"AI CHOOSED: {ai_choice} You Choose: {user_choice} -----> YOU WIN"
                    result_color = "green"
            else:
                result_text = f"AI CHOOSED: {ai_choice}-----> YOU LOSE"
                result_color = "red"

            Design_instance.result_label = tk.Label(
                Design_instance.f5,
                text=result_text,
                font=("Arial", 20, "bold"),
                bg="blue",
                fg=result_color
            )
            Design_instance.result_label.pack(pady=10)

# GUESS THE NUMBER FUNCTION
def gtn():
    global ai_choice
    Design_instance.reset_main_design()
    root.configure(bg="blue")
    Design_instance.f5.config(bg="blue")
    ai_choice = random.randint(1, 100)
    label = tk.Label(Design_instance.f5, text="GUESS THE NUMBER: ", font=("Arial", 20, "bold"), bg="blue", fg="white")
    label.pack()
    entry = tk.Entry(Design_instance.f5, font=("Arial", 20, "bold"), bg="blue", fg="white", textvariable=num)
    entry.pack()
    button = tk.Button(Design_instance.f5, text="BACK", font=("Arial", 20, "bold"), bg="blue", fg="white", borderwidth=0, command=lambda: click_gtn("BACK"))
    button.pack()
    button1 = tk.Button(Design_instance.f5, text="Done", font=("Arial", 20, "bold"), bg="blue", fg="white", borderwidth=0, command=lambda: click_gtn("SUBMIT"))
    button1.pack()

# MAIN SCREEN CLICK FUNCTION
def click(idx):
    if idx == "ROCK-PAPER-SCISSOR":
        rps()
    elif idx == "GUESS THE NUMBER":
        gtn()
    elif idx == "EXIT":
        root.destroy()

# MAIN SCREEN DESIGN
class Design:
    def __init__(self,master):
        self.f1 = tk.Frame(master, bg="red")
        self.f2 = tk.Frame(master, bg="red")
        self.f3 = tk.Frame(master, bg="red")
        self.f4 = tk.Frame(master, bg="red")
        self.f5 = tk.Frame(master, bg="hot pink")
        self.l1 = tk.Label(self.f1, text="WELCOME TO ROCK PAPER SCISSOR AND GUESS THE NUMBER GAME", font=("Arial", 16), bg="red", fg="white", height="2")
        self.l2 = tk.Label(self.f2, text="", bg="red", fg="white", width="4")
        self.l3 = tk.Label(self.f3, text="", bg="red", fg="white", width="4")
        self.l4 = tk.Label(self.f4, text="", bg="red", fg="white", height="2")
        self.f1.pack(side="top", fill="x")
        self.f2.pack(side="left", fill="y")
        self.f3.pack(side="right", fill="y")
        self.f4.pack(side="bottom", fill="x")
        self.f5.pack(expand=True)
        self.l1.pack(side="top")
        self.l2.pack()
        self.l3.pack()
        self.l4.pack()

        for i, option in enumerate(["ROCK-PAPER-SCISSOR", "GUESS THE NUMBER", "EXIT"]):
            self.button = tk.Button(
                self.f5,
                text=option,
                font=("Arial", 20, "bold"),
                bg="hot pink",
                fg="black",
                borderwidth=0,
                command=lambda idx=option: click(idx)
            )
            self.button.pack(pady=1)
    def reset_main_design(self):
        self.f1.destroy()
        self.f2.destroy()
        self.f3.destroy()
        self.f4.destroy()
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        for widget in self.f5.winfo_children():
            widget.destroy()

Design_instance = Design(root)

root.mainloop()