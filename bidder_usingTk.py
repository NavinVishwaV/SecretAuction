import tkinter as tk
from tkinter import messagebox, font

bids = {}
largest = 0

def bidding(name, bid):
    global largest
    bids[name] = bid
    if bid > largest:
        largest = bid

def submit_bid():
    global bids
    name = name_entry.get().strip()
    bid = bid_entry.get().strip()
    
    if name and bid.isdigit():
        bid = int(bid)
        bidding(name, bid)
        name_entry.delete(0, tk.END)
        bid_entry.delete(0, tk.END)
        messagebox.showinfo("Bid Submitted", f"Bid of {bid} from {name} added!")
    else:
        messagebox.showerror("Input Error", "Please enter a valid name and bid.")

def end_bidding():
    if bids:
        highest_bidder = max(bids, key=bids.get)
        messagebox.showinfo("Highest Bidder", f"The highest bidder is {highest_bidder} with a bid of {bids[highest_bidder]}")
    else:
        messagebox.showwarning("No Bids", "No bids were placed.")
    root.quit()

# Set up the main window
root = tk.Tk()
root.title("Bidding System")
root.geometry("400x300")
root.minsize(300, 200)

# Set a style
custom_font = font.Font(family="Helvetica", size=12)

# Create input fields with grid layout
tk.Label(root, text="Enter your name:", font=custom_font).grid(row=0, column=0, padx=10, pady=10, sticky='ew')
name_entry = tk.Entry(root, font=custom_font)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

tk.Label(root, text="Enter your bid:", font=custom_font).grid(row=1, column=0, padx=10, pady=10, sticky='ew')
bid_entry = tk.Entry(root, font=custom_font)
bid_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

# Create buttons with improved style
submit_button = tk.Button(root, text="Submit Bid", command=submit_bid, font=custom_font, bg="#4CAF50", fg="black")  # White text
submit_button.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

end_button = tk.Button(root, text="End Bidding", command=end_bidding, font=custom_font, bg="#f44336", fg="black")  # White text
end_button.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

# Configure grid weights to make the layout responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()
