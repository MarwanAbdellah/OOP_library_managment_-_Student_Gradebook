# Personal Library Management System

## Project Overview
The **Personal Library Management System** is a Python-based application designed to help users efficiently manage their personal book collections. The system allows users to add, remove, search, and display books while keeping data persistent across program executions.

This project was initially built with Object-Oriented Programming (OOP) concepts and later enhanced to include graphical user interfaces (GUIs) using the **Tkinter** library, converting the command-line functionalities into user-friendly applications.

## Features
- **Add Books:** Insert new book entries with details such as title, author, genre, and publication year.
- **Remove Books:** Delete books from the library.
- **Search Books:** Find books by title or author.
- **Display Library:** Show the entire collection of books.
- **Data Persistence:** Save and load the library data using text or CSV files.
- **Error Handling:** Gracefully handle input validation and file operation errors.
- **Graphical User Interface:** User-friendly GUI applications built using Tkinter.

## Installation and Setup
To run the GUI applications, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd project-root
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Tkinter-based GUI application:
    ```bash
    python library_management_gui.py
    ```

> Note: The provided `.exe` files are pre-compiled versions for direct execution on Windows systems.

## Usage Instructions
1. **Running the Application:**
   Launch the GUI application and use the interactive interface to perform actions such as adding, removing, or searching for books.

2. **Data Persistence:**
   Ensure that the library data is correctly saved and loaded using the file management options in the GUI.

## Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI library for creating desktop applications.
- **Object-Oriented Programming (OOP)**: Software development paradigm for code modularity and reuse.
- **File Handling**: Managing persistent storage of data using text and CSV files.

## Future Improvements
- Integration with external book APIs for automatic data fetching.
- Enhanced search functionalities.
- Sorting and filtering book lists.
- User rating and review features.
- Cross-platform GUI compatibility.

## Acknowledgments
Thanks to the initial project requirements that inspired the development of this application, with OOP concepts forming a strong foundation for software development.
