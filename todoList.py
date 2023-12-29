import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []

        self.task_var = tk.StringVar()

        # Entry widget for task input
        self.entry_task = tk.Entry(master, textvariable=self.task_var, width=40)
        self.entry_task.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for operations
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=2, padx=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=3, padx=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Bind double-click event to listbox
        self.task_listbox.bind("<Double-Button-1>", self.load_selected_task)

        # Populate the listbox with initial tasks
        self.update_task_listbox()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.clear_entry()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_var.get()
            if task:
                self.tasks[selected_index[0]] = task
                self.update_task_listbox()
                self.clear_entry()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            messagebox.showinfo("Task Deleted", f"Task '{task}' deleted.")
            self.update_task_listbox()

    def load_selected_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.task_var.set(selected_task)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def clear_entry(self):
        self.task_var.set("")
        self.entry_task.focus()

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
