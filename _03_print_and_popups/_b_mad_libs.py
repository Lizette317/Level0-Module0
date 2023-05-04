from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # Make a new window variable, window = Tk()

    # Hide the window using the window's .withdraw() method

    # Put this sentence in a pop-up message box:
    simpledialog.askstring(title='Greeter', prompt="If you find yourself having to cross a piranha-infested river, "
                                                   "here is how to do it...\n"
                                          "are you ready???")

    # Get the player to enter an adjective
    adj = simpledialog.askstring(title='adj', prompt="enter an adjective")
    # Get the player to enter a type of liquid
    tol = simpledialog.askstring(title='type of liquid', prompt="enter a type of liquid")
    # Get the player to enter a body part
    bp = simpledialog.askstring(title='body part', prompt="enter a part of your body")
    # Get the player to enter a verb
    v = simpledialog.askstring(title='verb', prompt="enter a verb")
    # Get the player to enter a place
    p = simpledialog.askstring(title='place', prompt="enter a place")
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more " + adj + " during the day, so cross the river at\n"
        "night. Piranhas are attracted to fresh " + tol + " and will most\n"
        "likely take a bite out of your " + bp + " if you " + v + ". Whatever\n"
        "you do, if you have an open wound, try to find another way\n"
        "to get back to the " + p + ". Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up
    simpledialog.askstring(title="cool thing", prompt=story)

    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.
    window.mainloop()
    # Run the window's .mainloop() method

    pass
