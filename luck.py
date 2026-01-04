import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Arun", "Beena", "Charan", "Divya", "Esha", None, "Gopal", "Harini"],
    "Age": [20, 21, None, 22, None, 23, None, 21],
    "Marks": [85, 90, 78, None, None, 88, 92, None],
    "Gender": ["M", None, "M", "F", None, "M", None, "F"],
    "Department": ["CSE", "ECE", None, "IT", "CSE", None, "EEE", None],
    "Attendance_Percent": [92, None, 85, 88, None, 90, None, 95],
    "Scholarship": ["Yes", None, "No", None, "Yes", "No", None, None],
    "Hostel": ["Yes", "No", None, "Yes", None, None, "Yes", None],
    "Year": [2, 2, None, 3, 1, None, 4, 2]
}

df = pd.DataFrame(data)
# cleaning
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Gender"].fillna("Not Specified", inplace=True)
df["Department"].fillna("Unknown", inplace=True)
df["Attendance_Percent"].fillna(df["Attendance_Percent"].mean(), inplace=True)
df["Scholarship"].fillna("No", inplace=True)
df["Hostel"].fillna("No", inplace=True)
df["Year"].fillna(df["Year"].mode()[0], inplace=True)
print(df)
