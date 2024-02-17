import csv
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import string

class CSVLoader:
    """
    A class for loading, adding, and deleting data from a CSV file.
    """
    def __init__(self, master):
        self.data = []
        self.categories = []
        self.root = master
        self.root.geometry("900x100")
        self.text_panel = None

    def load_data(self):
        """
        Load data from a CSV file.
        """
        file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.root.geometry("900x800")
                csv_reader = csv.reader(file)
                self.categories = next(csv_reader)[1:]  # Exclude the first column (ID) from categories
                for row in csv_reader:
                    self.data.append(row)
            self.display_data()

    def delete_data(self, record_id=None):
        """
        Delete data with the specified ID.
        """
        if record_id is None:
            record_id = simpledialog.askstring("Input", "Enter ID to delete:")
            if record_id is None:
                return
        for row in self.data:
            if row[0] == record_id:
                self.data.remove(row)
                break
        self.display_data()

    def add_data(self):
        """
        Add new data record.
        """
        try:
            if not self.data:
                messagebox.showinfo("Add Data", "No data loaded.")
                return

            new_id = simpledialog.askstring("Input", "Enter ID:")
            if new_id is None:
                return  # User canceled

            # Check if the ID is already used
            if any(row[0] == new_id for row in self.data):
                messagebox.showerror("Error", "A record with this ID already exists.")
                return

            # Check if the ID was previously deleted
            for i, row in enumerate(self.data):
                if row[0] == new_id:
                    del self.data[i]  # Remove the deleted row
                    messagebox.showwarning("Warning", "The ID was previously deleted and has been restored.")
                    break

            new_record = {'ID': new_id}
            for i, field in enumerate(self.categories):
                new_record[field] = simpledialog.askstring("Input", f"Enter {field}:")

            self.data.append([new_record[field] for field in ['ID'] + self.categories])
            self.data.sort(key=lambda x: int(x[0]))  # Sort by ID (assuming IDs are integers)
            self.display_data()
            messagebox.showinfo("Add Data", "New record added successfully.")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid value: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding data:\n\n{e}")

    def display_data(self, row=None):
        """
        Display loaded data or specific row data.
        """
        if self.text_panel:
            self.text_panel.destroy()

        self.text_panel = tk.Text(self.root, width=80, height=40)
        self.text_panel.pack(expand=False, fill=tk.BOTH, padx=20, pady=(20, 0))  # Adjusted pady to add top padding

        self.text_panel.insert(tk.END, "Data:\n")
        self.text_panel.insert(tk.END, "Categories: " + ", ".join(self.categories) + "\n\n")

        if row is None:
            for row in self.data:
                self.text_panel.insert(tk.END, f"ID: {row[0]}\n")
                for i, value in enumerate(row[1:]):
                    self.text_panel.insert(tk.END, f"\t{self.categories[i]}: {value}\n")
        else:
            self.text_panel.insert(tk.END, f"ID: {row[0]}\n")
            for i, value in enumerate(row[1:]):
                self.text_panel.insert(tk.END, f"\t{self.categories[i]}: {value}\n")

    def search_data(self, search_id):
        """
        Search for data by ID and display if found.
        """
        if not self.data:
            messagebox.showinfo("Search Data", "No data loaded.")
            return

        found = False
        for row in self.data:
            if row[0] == search_id:
                found = True
                messagebox.showinfo("Search Data", f"ID {search_id} found!")
                self.original_data = self.data[:]  # Store the original data
                self.display_data(row)  # Display the found data
                break

        if not found:
            messagebox.showinfo("Search Data", f"ID {search_id} not found.")


    def display_all_data(self):
        """
        Display all original loaded data.
        """
        if not self.original_data:
            messagebox.showinfo("Display All Data", "No data to display.")
            return

        self.data = self.original_data[:]  # Restore the original data
        self.display_data()

# Modify the on_button_click function to handle the Search Data and Display All Data buttons click
def on_button_click(clicked_index):
    if clicked_index == 0:
        csv_loader.load_data()
    elif clicked_index == 1:
        csv_loader.add_data()
    elif clicked_index == 2:
        csv_loader.delete_data()
    elif clicked_index == 3:
        search_id = simpledialog.askstring("Search Data", "Enter ID to search:")
        if search_id is not None:
            csv_loader.search_data(search_id)
    elif clicked_index == 4:
        csv_loader.display_all_data()  # Handle the Display All Data button click
    else:
        pass

def delete_data_callback():
    """
    Callback function for deleting data.
    """
    csv_loader.delete_data()

def add_data_callback():
    """
    Callback function for adding data.
    """
    csv_loader.add_data()

root = tk.Tk()
root.title("CSV Loader")

# User Agreement
agreement_text = """
User Agreement:
Data Privacy:
- Your data privacy is important to us.
- We collect and process data only for the purpose 
  of this application's functionality.
- We do not share your personal information with 
  third parties without your consent.
Application Sharing:
- You may use the application on your personal 
  devices.
- Sharing your application credentials with others 
  is prohibited.
- Each user should have a separate account.
Data Usage:
- You may not sell or distribute data generated or 
  collected by this application.
- Any such actions require the express consent of 
  Forestview, the application owner.
Security Measures:
- We conduct periodic vulnerability assessments to 
  ensure the security of our system.
- Preventive actions are taken based on the 
  outcomes of these assessments.
Vendor Requirements:
- We demand that all our key vendors adhere to 
  strict security standards.
- Vendors must also perform periodic vulnerability 
  assessments and take preventive actions.
Change of Requirements:
- As technology and the overall security landscape 
  evolve, requirements for using this application may 
  change.
- Users will be notified of any changes through the 
  application's official communication channels.
Disclaimer:
- This application is provided "as is" without any 
  warranties.
- Forestview is not responsible for any data 
  breaches, losses, or damages.
Indemnity Clause:
- By using this application, you agree to indemnify 
  Forestview from any legal ramifications
  arising from data breaches, zero-day attacks, and 
  database worms, including SQL injection.
By proceeding, you accept the terms of this 
agreement.
"""

if messagebox.askyesno("User Agreement", agreement_text):
    csv_loader = CSVLoader(root)

    frame = tk.Frame(root)
    frame.pack(expand=False, fill=tk.BOTH)

    buttons = []
    BUTTON_TEXTS = ["Load Data", "Add Data", "Delete Data", "Search Data", "Display All Data"]  # Add "Display All Data" button
    for i, text in enumerate(BUTTON_TEXTS):
        btn = tk.Button(frame, text=text, height=3, width=20, command=lambda i=i: on_button_click(i))
        btn.pack(side=tk.LEFT, padx=10, pady=10)  # Pack buttons to the left side with padding
        buttons.append(btn)

    root.mainloop()
else:
    messagebox.showinfo("User Agreement", "You must accept the user agreement to proceed.")
