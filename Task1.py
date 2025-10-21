import tkinter as tk
from tkinter import messagebox
import json
import os

# ---------- File for storing data ----------
DATA_FILE = "tasks.json"

# ---------- Load existing tasks ----------
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# ---------- Save tasks to file ----------
def save_tasks():
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------- Add a new task ----------
def add_task():
    task = entry_task.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append({"task": task, "done": False})
    entry_task.delete(0, tk.END)
    update_listbox()
    save_tasks()

# ---------- Delete selected task ----------
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# ---------- Mark as completed ----------
def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks[selected_index]["done"] = True
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# ---------- Edit selected task ----------
def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get().strip()
        if new_task == "":
            messagebox.showwarning("Warning", "Please enter a new task name!")
            return
        tasks[selected_index]["task"] = new_task
        update_listbox()
        save_tasks()
        entry_task.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# ---------- Update listbox display ----------
def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        display = f"[✔] {task['task']}" if task["done"] else f"[ ] {task['task']}"
        listbox_tasks.insert(tk.END, display)

# ---------- Exit the app ----------
def exit_app():
    save_tasks()
    root.destroy()

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("CodeSoft To-Do List")
root.geometry("400x450")
root.config(bg="#e6f3ff")

tasks = load_tasks()

# ---------- UI Components ----------
tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"), bg="#e6f3ff", fg="#333").pack(pady=10)

frame = tk.Frame(root, bg="#e6f3ff")
frame.pack(pady=5)

entry_task = tk.Entry(frame, width=25, font=("Arial", 12))
entry_task.grid(row=0, column=0, padx=5)

btn_add = tk.Button(frame, text="Add", width=8, command=add_task, bg="#007bff", fg="white")
btn_add.grid(row=0, column=1)

listbox_tasks = tk.Listbox(root, width=45, height=12, font=("Arial", 12))
listbox_tasks.pack(pady=10)

btn_frame = tk.Frame(root, bg="#e6f3ff")
btn_frame.pack()

tk.Button(btn_frame, text="Delete", width=10, command=delete_task, bg="#dc3545", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Edit", width=10, command=edit_task, bg="#ffc107", fg="black").grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Complete", width=10, command=mark_completed, bg="#28a745", fg="white").grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Exit", width=10, command=exit_app, bg="#6c757d", fg="white").grid(row=1, column=1, pady=10)

update_listbox()

root.mainloop()
