import tkinter as tk
from tkinter import scrolledtext

def save_note():
    note = text.get("1.0", tk.END)
    var=input("tell the file name - ")
    with open(var, "a") as file:
        file.write(note)
    text.delete("1.0", tk.END)
    status_label.config(text="Note saved!")

# Create the main window
window = tk.Tk()
window.title("Note Taking App")

# Create a text area for writing notes
text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=10)
text.pack(padx=0, pady=0)

# Create a "Save" button to save the note
save_button = tk.Button(window, text="Save Note", command=save_note)
save_button.pack(padx=10, pady=5)

# Create a status label
status_label = tk.Label(window, text="", fg="green")
status_label.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()