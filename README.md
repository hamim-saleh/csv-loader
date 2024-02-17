# CSVLoader Class

The `CSVLoader` class is a simple Python class designed to handle loading, adding, deleting, and displaying data from a CSV file using a graphical user interface (GUI) built with Tkinter.

## Features

- Load data from a CSV file.
- Add new data records to the loaded data.
- Delete data records by ID.
- Display all loaded data or specific row data.
- Search for data by ID and display if found.

## Usage

1. Import the `CSVLoader` class into your Python script or module.
2. Create an instance of the `CSVLoader` class, passing a Tkinter master window as an argument.
3. Use the methods of the `CSVLoader` instance to interact with data:
    - `load_data()`: Load data from a CSV file.
    - `add_data()`: Add new data records.
    - `delete_data(record_id)`: Delete data records by ID.
    - `display_data(row)`: Display all loaded data or specific row data.
    - `search_data(search_id)`: Search for data by ID and display if found.
    - `display_all_data()`: Display all original loaded data.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installations)

## Example

```python
import tkinter as tk
from CSVLoader import CSVLoader

root = tk.Tk()
root.title("CSV Loader")

csv_loader = CSVLoader(root)

# Add buttons and other GUI elements as needed

root.mainloop()
