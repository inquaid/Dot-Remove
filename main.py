import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

def delete_files():
    folder_path = path_entry.get()
    extensions = extensions_entry.get().split()

    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified folder does not exist.")
        return

    deleted_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                try:
                    os.remove(os.path.join(root, file))
                    deleted_files.append(file)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete {file}: {e}")

    messagebox.showinfo("Success", f"Deleted {len(deleted_files)} file(s) with extensions: {', '.join(extensions)}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, ctk.END)
    path_entry.insert(0, folder_selected)

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Dot_Remove")
root.geometry("700x250")


# folder selection widgets
path_label = ctk.CTkLabel(root, text="Select Folder:")
path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
path_entry = ctk.CTkEntry(root, width=300)
path_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = ctk.CTkButton(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=10, pady=10)

extensions_label = ctk.CTkLabel(root, text="File Extensions (space-separated):")
extensions_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
extensions_entry = ctk.CTkEntry(root, width=300)
extensions_entry.grid(row=1, column=1, padx=10, pady=10)

delete_button = ctk.CTkButton(root, text="Delete Files", command=delete_files)
delete_button.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
