from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# Make a new window variable, window = Tk()

# Hide the window using the window's .withdraw() method

# 1. Create a variable to hold the user's score. Set it equal to zero.
s = 0
# ASK A QUESTION AND CHECK THE ANSWER

#      // 2.  Ask the user a question
q = simpledialog.askstring(title='question', prompt="Who is the president of the United States?")
#      // 3.  Use an if statement to check if their answer is correct
if q == "Joe Biden" or q == "joe biden" or q == "Joe biden" or q == "President Joe Biden":
    s = s + 1
else:
    s = s - 1
q2 = simpledialog.askstring(title='question', prompt="How long is New Zealand's Ninety Mile Beach?")
if q2 == "55" or q2 == "55 miles":
    s = s+1
else:
    s = s-1
q3 = simpledialog.askstring(title='question', prompt="What was Elvis Presley's first hit in the U.S.?")
if q3 == "Heartbreak Hotel" or q3 == "heartbreak hotel" or q3 == "Heartbreak hotel":
    s = s+1
else:
    s = s-1
q4 = simpledialog.askstring(title='question', prompt="Van Halen famously banned which color of M&M's from backstage "
                                                     "at their concerts?")
if q4 == "Brown" or q4 == "brown":
    s = s+1
else:
    s = s-1
q5 = simpledialog.askstring(title='question', prompt="How many octaves can Ariana Grande sing?")
if q5 == "4" or q5 == "4 octaves":
    s = s+1
else:
    s = s-1
print("your final score was " + str(s) + "!")
#      // 4.  if the user's answer was correct, add one to their score

# MAKE MORE QUESTIONS. Ask more questions by repeating the above
#      // Option: Subtract a point from their score for a wrong answer

# After all the questions have been asked, tell the user their final score
# remember to convert your variable to a string using the str() function

# Run the window's .mainloop() method
window.mainloop()
