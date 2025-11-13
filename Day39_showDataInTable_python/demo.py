import tkinter as tk
from tkinter import ttk

data_columns=["Item Id","Product Name","Price(INR)","Stock"]
sample_data=[
    (100,"Product 1",850,45),
    (101,"Product 2",800,55),
    (102,"Product 3",400,75),
    (103,"Product 4",300,25),
    (104,"Product 5",600,35),
    (105,"Product 6",950,85),
]

def create_table_gui():
    root=tk.Tk()
    root.title("Data table using Treeview")
    root.geometry("400x400")

    tree=ttk.Treeview(root,columns=data_columns,show='headings',height=10)
    for col in data_columns:
        tree.column(col,anchor=tk.CENTER,width=120)
        tree.heading(col,text=col)
    
    for item in sample_data:
        tree.insert('',tk.END,values=item)

    tree.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
    root.mainloop()

if __name__=='__main__':
    create_table_gui()