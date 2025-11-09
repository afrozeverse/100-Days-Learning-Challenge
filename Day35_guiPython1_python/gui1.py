import tkinter as tk   # Import the tkinter module

root = tk.Tk()         # Create the main window
root.title("My First GUI")  # Set the window title
root.geometry("300x200")    # Set window size (width x height)

label = tk.Label(root, text="Hello, Tkinter!")  # Create a label
label.pack(pady=20)       # Add the label to the window with some space

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()             # Add the button to the window

root.mainloop()           # Run the GUI loop (keeps the window open)
