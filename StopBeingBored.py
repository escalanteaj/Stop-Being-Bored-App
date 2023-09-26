import tkinter as tk
import requests

# Define the color palette
WINDOW_BG = "#321c3d"
LABEL_COLOR = "#ee5927"
BUTTON_COLOR = "#d4bbd8"
TEXT_COLOR = "#FFFFFF"
BUTTON_TEXT_COLOR = "#000000"

# Function to fetch a new activity from the API
def get_random_activity():
    response = requests.get("https://www.boredapi.com/api/activity")
    data = response.json()
    return data

# Function to update the activity displayed on the GUI
def refresh_activity():
    activity_data = get_random_activity()
    activity_label.config(text=activity_data["activity"])
    participants_label.config(text=f"Participants: {activity_data['participants']}")
    price_label.config(text=f"Price: {activity_data['price']}")
    if activity_data["link"]:
        website_link.config(text="Link to learn more", command=lambda link=activity_data['link']: open_website(link), state="normal")
    else:
        website_link.config(text="No link", command=None, state="disabled")

# Function to open a webpage in a browser
def open_website(link):
    import webbrowser
    webbrowser.open(link)

# Create the main window
root = tk.Tk()
root.title("Stop Being Bored")
root.geometry("300x450")
root.configure(bg=WINDOW_BG)

# Create and configure labels
activity_label = tk.Label(root, text="", bg=LABEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12), wraplength=250, justify="center")
participants_label = tk.Label(root, text="", bg=LABEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10))
price_label = tk.Label(root, text="", bg=LABEL_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10))

# Create and configure the "Link to learn more" button
website_link = tk.Button(root, text="", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Helvetica", 10), state="disabled")

# Create and configure the "Refresh" button
refresh_button = tk.Button(root, text="Refresh", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Helvetica", 12), command=refresh_activity)

# Place widgets using pack with expand and fill
activity_label.pack(fill="both", expand=True, padx=10, pady=(10, 5))
participants_label.pack(fill="both", expand=True, padx=10, pady=5)
price_label.pack(fill="both", expand=True, padx=10, pady=5)
website_link.pack(fill="both", expand=True, padx=10, pady=(5, 10))
refresh_button.pack(fill="both", expand=True, padx=10, pady=(0, 10))

# Initial activity load
refresh_activity()

# Start the Tkinter main loop
root.mainloop()
