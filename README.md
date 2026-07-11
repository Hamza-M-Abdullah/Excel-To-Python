# Excel to PY: Student Grade Calculator 📊🐍

A beginner-friendly Python script using the **Pandas** library to automate data processing from an Excel spreadsheet. This project is designed as a learning resource to show how to clean data, perform vectorized math, and map custom logic onto data frames.

---

## 🚀 Features

* **Data Cleaning:** Automatically skips empty header rows and removes useless blank columns from raw Excel files.
* **Vectorized Operations:** Calculates student percentages instantly across entire columns without slow row-by-row loops.
* **Compact Logic:** Uses a single-line Python conditional expression (ternary operators) to evaluate numeric scores into letter grades.
* **Excel Automation:** Outputs the beautifully sorted and graded data into a brand-new Excel sheet without altering the original file.

---

## 🛠️ Code Breakdown

Here is a quick look at the core logic used in this project:

```python
# The heart of the grading logic using a single-line chained if-else statement
def get_student_grade(points):
    return "A+" if points >= 90 else "A" if points >= 80 else "B" if points >= 70 else "C" if points >= 60 else "D" if points >= 50 else "F"

# Vectorized percentage math (Points / Max Marks * 100)
sortexam['Percentage'] = (sortexam['Points'] / sortexam['Max Marks']) * 100

# Mapping the grading function to the DataFrame
sortexam['Grade'] = sortexam['Points'].apply(get_student_grade)
