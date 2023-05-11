from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# Make a new window variable, window = Tk()

# Hide the window using the window's .withdraw() method

# 1. Ask the user if they know how to write code.
s = simpledialog.askstring(title="code", prompt="do you know how to write code?")
# 2. If they say "yes", tell them they will rule the world in a message box pop-up.
if s == "yes":
    messagebox.Message("You will rule the world!")
    print()
    messagebox.showinfo()

else:
    messagebox.Message("sign up for a coding class!")
    print()
    messagebox.showerror()

# 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.

# Run the window's .mainloop() method
    window.mainloop()
