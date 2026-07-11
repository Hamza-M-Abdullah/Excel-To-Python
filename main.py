# Importent Note

# if you run this code, it will read the 'exam.xlsx' file, sort the data by 'Points', calculate the average points, assign grades based on the points, and then save the updated data to a new Excel file called 'exam_updated.xlsx'. If you want to overwrite the original file, it will also save the updated data back to 'exam.xlsx' remeber dont use code twice with same name it will just auto write it again.

import pandas as pd

import matplotlib.pyplot as plt # A libraray for excel of bar and charts

# This will Load the raw data from the spreadsheet calles exam.xlsx and store it in a DataFrame called exam. The DataFrame is a two-dimensional data structure that can hold data of different types (e.g., integers, strings, floats) and is similar to a table in a database or an Excel spreadsheet.

exam = pd.read_excel('exam.xlsx')

print("--- Excel File Content ---")
print("--------------------------")

# This will sort the DataFrame by the 'Points' column in descending order (highest to lowest) and store the sorted DataFrame in a new variable called sortexam. The sort_values() function is used to perform the sorting operation Here ascending=False will tell the python to sort in descending order.

sortexam = exam.sort_values(by='Points', ascending=False)


print("--------------------------")
print("Average Points:", exam['Points'].mean())
print("--------------------------")

# This function takes a student's points as input and returns the corresponding grade based on the specified criteria. The function uses a series of conditional statements (if-else) to determine the grade based on the points. Here see the if-else statement used in single line that is ruturning the grade. Its fun right.

def get_student_grade(points):
    return "A+" if points >= 90 else "A" if points >= 80 else "B" if points >= 70 else "C" if points >= 60 else "D" if points >= 50 else "F"

# This will calculate the percentage of points obtained by each student and store it in a new column called 'Percentage' in the sortexam DataFrame. The percentage is calculated by dividing the 'Points' by the 'Max Marks' and multiplying by 100. Then it will assign grades to each student based on their points using the get_student_grade function and store the grades in a new column called 'Grade'.

sortexam['Percentage'] = (sortexam['Points'] / sortexam['Max Marks']) * 100
sortexam['Grade'] = sortexam['Points'].apply(get_student_grade)
print(sortexam)

print("--------------------------")

# # ==========================================
# # NEW FEATURE: GENERATING A GRADE CHART Bar Chart📊
# # ==========================================

# # Count how many students got each grade (e.g., A+: 3, B: 5)
# # .value_counts() groups identical items together and counts them
# grade_counts = sortexam['Grade'].value_counts()

# # Create a new figure/window for the chart
# plt.figure(figsize=(8, 5))

# # Build a bar chart using the grades as labels and counts as the height
# plt.bar(grade_counts.index, grade_counts.values, color='skyblue', edgecolor='black')

# # Add titles and labels to read it easily
# plt.title('Distribution of Student Grades', fontsize=14, fontweight='bold')
# plt.xlabel('Letter Grades', fontsize=12)
# plt.ylabel('Number of Students', fontsize=12)

# # Save the visual chart as a PNG image inside your folder
# plt.savefig('grade_distribution.png', dpi=300)

# # Clean up the chart memory
# plt.close()

# print("🎉 Success! Chart saved as 'grade_distribution.png'")
# print("--------------------------")

# ==========================================
# NEW FEATURE: GENERATING A PIE CHART 🍕
# ==========================================

# 1. Count how many students got each grade
grade_counts = sortexam['Grade'].value_counts()

# 2. Define a custom color map matching your rules
# Green for top grades, red for failing, distinct colors for the rest
color_map = {
    'A+': '#27ae60',   # Darker Green
    'A': '#2ecc71',  # Bright Green
    'B': '#3498db',   # Blue
    'C': '#f1c40f',   # Yellow
    'D': '#e67e22',   # Orange
    'F': '#e74c3c'    # Bright Red
}

# Match the colors dynamically to whatever grades exist in your data
custom_colors = [color_map[grade] for grade in grade_counts.index]

# 3. Create the pie chart canvas
plt.figure(figsize=(7, 7))  # Equilateral size keeps the circle perfectly round

# 4. Plot the pie chart
plt.pie(
    grade_counts.values,          # The data counts
    labels=grade_counts.index,    # Grade letters on the outside
    colors=custom_colors,         # Your custom green/red color scheme
    autopct='%1.1f%%',            # Automatically calculate and display percentages
    startangle=140,               # Rotates the starting position for a cleaner look
    textprops={'fontsize': 12, 'weight': 'bold'}  # Clean, bold font for readability
)

# Set the title
plt.title('Student Grade Distribution (Pie Chart)', fontsize=14, fontweight='bold')

# Save the circle chart as a PNG image inside your folder
plt.savefig('grade_distribution_pie.png', dpi=300)
plt.close()

print("🎉 Success! Circle chart saved as 'grade_distribution_pie.png'")
print("--------------------------")

#Here see the index=False argument it is used to exclude the index column from being written to the Excel file. If you want to include the index in the output file, you can set index=True instead or dont use it.

sortexam.to_excel('exam_updated.xlsx', index=False) 

#This will make a new excel file with the updated data. If you want to overwrite the existing file, you can use the same filename 'exam.xlsx' instead of 'exam_updated.xlsx'.

# like this

sortexam.to_excel('exam.xlsx', index=False)