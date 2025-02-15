import subprocess
import random

love_notes = [
    "If (you == mine) { myHeart.explode(); }",
    "You and me are like RAM and CPU—inseparable and overheating together.",
    "Roses are #FF0000, Violets are #0000FF, I have an infinite loop, and the only escape condition is YOU."
]

def spam_love_notes():
    for _ in range(10):
        note = random.choice(love_notes)
        with open(f"note_{_}.txt", "w") as f:
            f.write(note)
        subprocess.Popen(["notepad.exe", f"note_{_}.txt"])

spam_love_notes()