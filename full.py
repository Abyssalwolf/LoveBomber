import tkinter as tk
from tkinter import messagebox
import subprocess
import random
import threading
import simpleaudio as sa
import sys
import os
import ctypes
import time
import win32com.client
import tempfile


# ============================
# Phase 1: Romantic Setup
# ============================
def phase_1():
    # Create the main window
    root = tk.Tk()
    root.title("Love Bomb.exe")
    root.geometry("800x600")
    root.configure(bg="pink")

    # Create a canvas with a gradient background
    canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Gradient background
    for i in range(600):
        gradient_color = f'#{int(255 - (i / 600 * 255)):02x}{int(255 - (i / 600 * 255)):02x}ff'
        canvas.create_line(0, i, 800, i, fill=gradient_color)

    # Add floating hearts (random animation)
    hearts = []
    heart_colors = ["red", "pink", "white"]
    animation_running = True  # Define animation_running in the enclosing scope

    def create_heart():
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        heart = canvas.create_text(x, y, text="❤️", font=("Arial", 24), fill=random.choice(heart_colors))
        hearts.append(heart)
        move_heart(heart)

    def move_heart(heart):
        if not animation_running:  # Stop animation if the flag is False
            return
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        canvas.move(heart, dx, dy)
        x, y = canvas.coords(heart)
        # Wrap around the screen
        if x > 800:
            canvas.move(heart, -800, 0)
        elif x < 0:
            canvas.move(heart, 800, 0)
        if y > 600:
            canvas.move(heart, 0, -600)
        elif y < 0:
            canvas.move(heart, 0, 600)
        canvas.after(50, move_heart, heart)

    # Create multiple hearts
    for _ in range(20):
        create_heart()

    # Popup message with custom styling
    def show_popup():
        nonlocal animation_running  # Now this works because animation_running is defined in the enclosing scope
        animation_running = False  # Stop the animation

        # Create a popup window
        popup = tk.Toplevel(root)
        popup.title("Special Valentine’s Gift ❤️")
        popup.geometry("400x200")
        popup.configure(bg="#ffcccb")

        # Add a label with custom font and shadow
        label = tk.Label(
            popup,
            text="Click 'Accept Love' to continue.",
            font=("Comic Sans MS", 16, "bold"),
            fg="red",
            bg="#ffcccb",
        )
        label.pack(pady=20)

        # Add a styled button
        def on_accept():
            popup.destroy()
            root.destroy()
            phase_2()

        accept_button = tk.Button(
            popup,
            text="Accept Love",
            font=("Comic Sans MS", 14),
            fg="white",
            bg="red",
            activebackground="pink",
            activeforeground="white",
            relief="raised",
            borderwidth=3,
            command=on_accept,
        )
        accept_button.pack(pady=10)

        # Add hover effect to the button
        def on_enter(e):
            accept_button.config(bg="pink", fg="red")

        def on_leave(e):
            accept_button.config(bg="red", fg="white")

        accept_button.bind("<Enter>", on_enter)
        accept_button.bind("<Leave>", on_leave)

    # Schedule the popup after 2 seconds
    root.after(2000, show_popup)
    root.mainloop()

# ============================
# Phase 2: Love Bomb Begins
# ============================
def spam_love_notes():
    love_notes = [
        "If (you == mine) { myHeart.explode(); }",
        "You and me are like RAM and CPU—inseparable and overheating together.",
        "Roses are #FF0000, Violets are #0000FF, I have an infinite loop, and the only escape condition is YOU.",
        "My love for you is like a recursive function—it keeps calling itself, deeper and deeper, until it reaches the base case of forever.",
        "You are the missing semicolon in my code; without you, everything falls apart.",
        "I tried to write a program to describe how much I love you, but I ran out of memory.",
        "You are the exception to all my rules. Without you, my life would throw a NullPointerException.",
        "Our love is like a binary tree—it grows exponentially with every passing moment.",
        "You are the CSS to my HTML—without you, I’m just plain and unstyled.",
        "I don’t need a debugger to know that you are the only solution to my problems.",
        "You are the API to my heart—every request I make returns a 200 OK.",
        "My love for you is like a blockchain—immutable, decentralized, and growing stronger with every block.",
        "You are the git to my commit—I can’t imagine my life without you.",
        "If love were a programming language, you’d be my favorite syntax.",
        "You are the async to my await—I’ll always wait for you, no matter how long it takes.",
        "Our love is like a well-optimized algorithm—efficient, elegant, and timeless.",
        "You are the key to my heart’s encryption—without you, I’m just a jumble of random bytes.",
        "I don’t need a compiler to tell me that you are the one for me.",
        "You are the stack to my heap—together, we make the perfect memory.",
        "My love for you is like a quantum state—it exists in all possible states until you observe it.",
    ]

    temp_dir = tempfile.gettempdir()  # Use a temporary directory
    for _ in range(10):  # Open 10 notes
        note = random.choice(love_notes)
        file_path = os.path.join(temp_dir, f"note_{_}.txt")
        with open(file_path, "w") as f:
            f.write(note)
        subprocess.Popen(["notepad.exe", file_path])

def play_audio(file_path):
    try:
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"Error playing audio: {e}")

def play_audio_in_thread(file_path):
    thread = threading.Thread(target=play_audio, args=(file_path,))
    thread.start()

# Paths to audio files
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
titanic_theme_path = os.path.join(ASSETS_DIR, "titanic_theme.wav")
ai_voice_love_path = os.path.join(ASSETS_DIR, "ai_voice_love.wav")
error_sound_path = os.path.join(ASSETS_DIR, "error_sound.wav")
lb_sound_path = os.path.join(ASSETS_DIR, "love_bomber.wav")

   # Play all sounds
def play_all_audio():
    play_audio_in_thread(titanic_theme_path)
    play_audio_in_thread(ai_voice_love_path)
    play_audio_in_thread(lb_sound_path)

def create_love_shortcuts():
    # Get the path to the user's desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Define some love-themed shortcut names (safe and ending with .lnk)
    love_shortcuts = [
        ("Our_Broken_Past_(broken_heart).lnk", "notepad.exe"),
        ("My_Heart_Occupied_By_You_(heart).lnk", "calc.exe"),  # Replaced <3 with (heart)
        ("Relationship_Status_Its_Complicated.lnk", "mspaint.exe"),
        ("Love_Letter_[love_letter].lnk", "notepad.exe"),
        ("Forever_Yours_(heart).lnk", "explorer.exe")  # Replaced <3 with (heart)
    ]

    # Create shortcuts using Windows Script Host
    shell = win32com.client.Dispatch("WScript.Shell")

    for name, target in love_shortcuts:
        shortcut_path = os.path.join(desktop_path, name)
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = target
        shortcut.Description = "A harmless love bomb shortcut ❤️"
        try:
            shortcut.Save()
            print(f"Created shortcut: {name}")
        except Exception as e:
            print(f"Failed to create shortcut '{name}': {e}")

def phase_2():
    spam_love_notes()
    play_all_audio()
    create_love_shortcuts()
    phase_3()  # Proceed to Phase 3

# ============================
# Phase 3: Escalation of Love
# ============================
def quiz_popup():
    choice = messagebox.askquestion(
        "Before you go…",
        "Do you love to the ends of the earth?",
        type=messagebox.YESNO
    )
    if choice != "yes":
        phase_2()  # More love bombing

def prevent_exit():
    attempts = 0
    while attempts < 5:  # Limit the number of attempts
        try:
            quiz_popup()
            break  # Exit the loop if the user selects "Yes"
        except KeyboardInterrupt:
            messagebox.showinfo("Love is Forever", "You thought you could escape love? Foolish mortal.")
            phase_2()
        attempts += 1
    else:
        messagebox.showinfo("Love is Forever", "You can't escape love forever!")
        sys.exit()

def phase_3():
    prevent_exit()
    final_bomb()

# ============================
# Phase 4: Final Bomb
# ============================
def final_bomb():
    # Create a fullscreen window
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    canvas = tk.Canvas(root, bg="pink")
    canvas.pack(fill="both", expand=True)

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Draw the heart at the center
    font_size = min(screen_width, screen_height) // 4  # Adjust divisor for desired scaling
    canvas.create_text(center_x, center_y, text="❤️", font=("Arial", font_size), fill="red")
    root.update()

    # Lock screen for 10 seconds
    ctypes.windll.user32.LockWorkStation()

    def farewell():
        root.destroy()
        messagebox.showinfo("Goodbye", "You’ll miss me. Goodbye, my love…")
        sys.exit()

    root.after(10000, farewell)  # Schedule farewell after 10 seconds
    root.mainloop()

# ============================
# Main Execution
# ============================
if __name__ == "__main__":
    try:
        phase_1()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)