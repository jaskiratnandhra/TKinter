
# Tkinter Projects with SQLite

This repository contains multiple projects built using **Tkinter**, the standard Python interface to the Tk GUI toolkit, along with **SQLite** as the database. These projects are designed to manage data related to different domains such as students, customers, employees, flight bookings, and more.

## Projects Overview

### 1. **Student Management System**
This project allows users to:
- Insert student information such as registration number, name, department, gender, and age.
- Update existing student records.
- Delete student records.
- Fetch and display student information.

### 2. **Customer Management System**
In this project, you can:
- Insert customer details including customer ID, name, branch, account type, and amount.
- Update existing customer information.
- Delete customer records.
- Fetch and display customer details from the SQLite database.

### 3. **Employee Management System**
This system enables:
- Managing employee details including employee ID, name, job title, employee type (Regular/Temporary), and salary.
- Inserting new employee records.
- Updating, deleting, and fetching existing employee information.

### 4. **Flight Booking System**
This application helps in managing flight bookings:
- Insert flight booking information like booking ID, passenger name, flight, source, destination, and duration.
- Update, delete, and fetch booking records.

### 5. **Movie Booking System**
This project helps manage movie bookings:
- Insert details like booking ID, person name, movie name, class (A/B), time of show, and the number of tickets.
- Update, delete, and fetch existing movie booking information.

## Technologies Used
- **Tkinter**: For the graphical user interface.
- **SQLite**: As the database to store and manage data.
- **Python**: As the core programming language.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tkinter-projects.git
   ```
2. Install the required Python packages:
   ```bash
   pip install tk sqlite3
   ```
3. Run the individual `.py` files for each project:
   ```bash
   python project_name.py
   ```

Each project comes with buttons for inserting, updating, deleting, and fetching data from the SQLite database.

## Project Structure
- Each `.py` file represents a different Tkinter project.
- The database used for each project is an SQLite file named `myTable.db`, created automatically upon running the code.
- User inputs are validated and managed via Entry widgets, Labels, Radiobuttons, and Spinbox/Scale for ease of data entry.

Feel free to explore the code and modify it as per your requirements!

## Contributions
Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.
