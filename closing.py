import sys

def quiz_popup():
    options = ["So much!", "You’re the love of my life.", "I can’t live without you."]
    choice = tk.messagebox.askquestion(
        "Before you go…",
        "How much do you love me?",
        type=tk.messagebox.YESNOCANCEL
    )
    if choice != "yes":
        phase_2()  # More love bombing

def prevent_exit():
    while True:
        try:
            phase_2()
        except KeyboardInterrupt:
            tk.messagebox.showinfo("Love is Forever", "You thought you could escape love? Foolish mortal.")
            phase_2()

prevent_exit()