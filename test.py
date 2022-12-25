from tkinter import *
import time
import random

root = Tk()
root.title("Typing Test")
root.config(bg="#FBE4F2")
root.geometry("670x270+100+100")

entryField = Entry(root, font=("arial", 20, "bold"), bg="#B89EF5",fg="#3B4252", bd=5, width=40)
entryField.grid(row=2, column=5)

text=Text(root,font=("palatino", 25, "bold"), width=20, height=1, bg="#FBE4F2",fg="#FC9743", borderwidth=1, relief="solid")
text.insert(END, "  Speed Typing Test")
text.config(state=DISABLED)
text.grid(row=0,column=5 )



def typing_speed_test_start():
    # Set the start time
    global start_time
    start_time = time.time()

def typing_speed_test_restart():
    entryField.delete("0", END)


def typing_speed_test_end():
    # Get the user's input
    user_input = entryField.get()

    # Get the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the typing speed
    typing_speed = len(user_input) / elapsed_time

    # Print the typing speed
   
    result.delete("1.0", END)
    result.insert(END, f"Your typing speed is {typing_speed:.2f} characters per second.")


result = Text(root,font=("palatino", 15, "bold"), width=33, height=2, bg="#FBE4F2")
result.insert(END, "Your typing speed will show here:")
result.grid(row=5, column=5)

text2 = Text(root,font=("palatino", 17, "bold" ), width=50, height=2, bg="#FBE4F2", borderwidth=1, relief="solid")
text2.insert(END, "Learning to type is a hard challenge. This is some random      typing that you can use to practice." )
text2.grid(row=1, column=5)

# Run the typing speed test
start_button = Button(root, text="Start", width=5, height=5, fg="red", bg="blue", command=typing_speed_test_start)
stop_button = Button(root, text="Stop", width=5, height=5, bg="blue", command= typing_speed_test_end)
restart_button = Button(root, text="Restart", width=5, height=5, fg="blue",bg="blue", command=typing_speed_test_restart)


start_button.grid(row=4, column=3)
stop_button.grid(row=4, column=5)
restart_button.grid(row=4, column=6)
root.mainloop()