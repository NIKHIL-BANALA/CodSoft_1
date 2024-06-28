import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_frame()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def edit_task(index):
    updated_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=tasks[index])
    if updated_task is not None:
        tasks[index] = updated_task
        update_frame()

def delete_task(index):
    tasks.pop(index)
    update_frame()

def update_frame():
    for widget in frame_tasks.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_frame = tk.Frame(frame_tasks, bg="white", highlightbackground="grey", highlightthickness=1)
        task_frame.pack(fill=tk.X, pady=2)

        label = tk.Label(task_frame, text=task, font=("Helvetica", 12), bg="white")
        label.pack(side=tk.LEFT, padx=5, pady=5)

        delete_button = tk.Button(task_frame, text="Delete", bg="red", fg="white", font=("Helvetica", 10), command=lambda index=index: delete_task(index))
        delete_button.pack(side=tk.RIGHT, padx=5)

        edit_button = tk.Button(task_frame, text="Edit", bg="green", fg="white", font=("Helvetica", 10), command=lambda index=index: edit_task(index))
        edit_button.pack(side=tk.RIGHT, padx=5)

tasks = []

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg='white')

head_frame = tk.Frame(root, bg="green")
head_frame.pack(pady=10, padx=10, fill="x")

label_heading = tk.Label(head_frame, text="To-Do List", font=("Helvetica", 22), bg="green", fg="white")
label_heading.pack(pady=10)

entry_frame = tk.Frame(root, bg="white")
entry_frame.pack(pady=10, padx=10, fill="x")

entry_task = tk.Entry(entry_frame, font=("Helvetica", 16))
entry_task.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

button_add = tk.Button(entry_frame, text="Add Task", font=("Helvetica", 12), bg="green", fg="white", command=add_task)
button_add.pack(side=tk.LEFT, padx=5)

frame_tasks = tk.Frame(root, bg="white")
frame_tasks.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
