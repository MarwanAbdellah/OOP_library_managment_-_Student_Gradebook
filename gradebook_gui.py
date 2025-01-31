import tkinter as tk
from tkinter import messagebox
import sys
import os
import csv

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            return True
        return False

    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].add_grade(subject, grade)
            self.save_data()
            return True
        return False

    def save_data(self):
        file_path = os.path.join(os.path.dirname(sys.argv[0]), "gradebook_data.csv")
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student Name", "Subject", "Grade"])
            for name, student in self.students.items():
                for subject, grade in student.grades.items():
                    writer.writerow([name, subject, grade])

gradebook = Gradebook()

def add_student():
    name = student_name_entry.get()
    if name:
        if gradebook.add_student(name):
            messagebox.showinfo("Success", "Student added successfully!")
            gradebook.save_data()
        else:
            messagebox.showwarning("Error", "Student already exists!")
    student_name_entry.delete(0, tk.END)

def add_grade():
    name = grade_student_entry.get()
    subject = subject_entry.get()
    try:
        grade = float(grade_entry.get())
        if gradebook.add_grade(name, subject, grade):
            messagebox.showinfo("Success", "Grade added successfully!")
        else:
            messagebox.showwarning("Error", "Student not found! Please add the student first.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid grade.")
    grade_student_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Gradebook")
root.geometry("500x350")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

frame = tk.Frame(root)
frame.pack(expand=True, padx=20, pady=20)

# Add Student
tk.Label(frame, text="Student Name:").grid(row=0, column=0, pady=5)
student_name_entry = tk.Entry(frame, width=30)
student_name_entry.grid(row=0, column=1, pady=5)
tk.Button(frame, text="Add Student", command=add_student).grid(row=0, column=2, padx=10, pady=5)

# Warning Label
tk.Label(frame, text="Note: You must add a student before assigning grades.", fg="red").grid(row=1, column=0, columnspan=3, pady=5)

# Add Grade
tk.Label(frame, text="Student Name:").grid(row=2, column=0, pady=5)
grade_student_entry = tk.Entry(frame, width=30)
grade_student_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Subject:").grid(row=3, column=0, pady=5)
subject_entry = tk.Entry(frame, width=30)
subject_entry.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Grade:").grid(row=4, column=0, pady=5)
grade_entry = tk.Entry(frame, width=30)
grade_entry.grid(row=4, column=1, pady=5)

tk.Button(frame, text="Add Grade", command=add_grade).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
