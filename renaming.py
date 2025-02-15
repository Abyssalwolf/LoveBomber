import os
import win32com.client

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

# Run the function
create_love_shortcuts()