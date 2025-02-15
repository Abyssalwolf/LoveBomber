import tkinter as tk
from tkinter import messagebox

def phase_1():
    # Create the main window
    root = tk.Tk()
    root.title("Love Bomb.exe")
    root.geometry("800x600")
    root.configure(bg="pink")

    # Add floating hearts (basic animation)
    canvas = tk.Canvas(root, bg="pink", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def animate_hearts():
        x, y = 0, 0
        for _ in range(50):
            canvas.create_text(x, y, text="❤️", font=("Arial", 24), fill="red")
            x += 20
            y += 20
            canvas.update()
            canvas.after(50)

    animate_hearts()

    # Popup message
    def show_popup():
        messagebox.showinfo("Special Valentine’s Gift ❤️", "Click 'Accept Love' to continue.")
        phase_2()  # Proceed to Phase 2

    root.after(2000, show_popup)  # Show popup after 2 seconds
    root.mainloop()

phase_1()