from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

player1_turn = True
count = 0

def check_win():
    global player1_turn, count
    if (b1["text"] == b2["text"] == b3["text"] == 'X' or
        b4["text"] == b5["text"] == b6["text"] == 'X' or
        b7["text"] == b8["text"] == b9["text"] == 'X' or
        b1["text"] == b4["text"] == b7["text"] == 'X' or
        b2["text"] == b5["text"] == b8["text"] == 'X' or
        b3["text"] == b6["text"] == b9["text"] == 'X' or
        b1["text"] == b5["text"] == b9["text"] == 'X' or
        b3["text"] == b5["text"] == b7["text"] == 'X'):
        messagebox.showinfo("Game Over", "Player 1 wins!")
        root.destroy()

    elif (b1["text"] == b2["text"] == b3["text"] == 'O' or
        b4["text"] == b5["text"] == b6["text"] == 'O' or
        b7["text"] == b8["text"] == b9["text"] == 'O' or
        b1["text"] == b4["text"] == b7["text"] == 'O' or
        b2["text"] == b5["text"] == b8["text"] == 'O' or
        b3["text"] == b6["text"] == b9["text"] == 'O' or
        b1["text"] == b5["text"] == b9["text"] == 'O' or
        b3["text"] == b5["text"] == b7["text"] == 'O'):
        messagebox.showinfo("Game Over", "Player 2 wins!")
        root.destroy()

    elif count == 9:
        messagebox.showinfo("Game Over", "It's a tie!")
        root.destroy()

def button_click(button):
    global player1_turn, count
    if button["text"] == "" and player1_turn:
        button["text"] = "X"
        player1_turn = False
        count += 1
        check_win()
    elif button["text"] == "" and not player1_turn:
        button["text"] = "O"
        player1_turn = True
        count += 1
        check_win()

# Create the buttons
b1 = Button(root, text="", height=5, width=10, command=lambda: button_click(b1))
b2 = Button(root, text="", height=5, width=10, command=lambda: button_click(b2))
b3 = Button(root, text="", height=5, width=10, command=lambda: button_click(b3))
b4 = Button(root, text="", height=5, width=10, command=lambda: button_click(b4))
b5 = Button(root, text="", height=5, width=10, command=lambda: button_click(b5))
b6 = Button(root, text="", height=5, width=10, command=lambda: button_click(b6))
b7 = Button(root, text="", height=5, width=10, command=lambda: button_click(b7))
b8 = Button(root, text="", height=5, width=10, command=lambda: button_click(b8))
b9 = Button(root, text="", height=5, width=10, command=lambda: button_click(b9))

# Grid layout
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()

