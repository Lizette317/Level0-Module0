from tkinter import messagebox, simpledialog, Tk
import random
# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# Make a new window variable, window = Tk()

# Hide the window using the window's .withdraw() method

# 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
n = random.randint(0, 3)
# 2. Print your variable to the console
# 3. Get the user to enter something that they think is awesome
input("Enter something that you think is awesome:")
# 4. If your variable is  0
# -- tell the user whatever they entered is awesome!

# 5. If your variable is  1
# -- tell the user whatever they entered is ok.

# 6. If your variable is  2
# -- tell the user whatever they entered is boring.

# 7. If your variable is  3
# -- invent your own message to give to the user (be nice).
if n == 0:
    print("What you entered is awesome!")
if n == 1:
    print("What you entered is ok i guess ")
if n == 2:
    print("what you entered is boring.")
if n == 3:
    print("please. anything but that. what you entered is terrible.")
# Run the window's .mainloop() method
window.mainloop()