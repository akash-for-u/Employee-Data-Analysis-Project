<<<<<<< HEAD
# 📘 Employee Data Analysis Project
# Author: Akash Soni

import pandas as pd
import matplotlib.pyplot as plt

# Step 1️⃣: Load dataset
df = pd.read_csv("employee.csv")

# Show first 5 rows and all column names
print("Here are the first 5 rows of your dataset:")
print(df.head())

print("\nThese are your column names:")
print(df.columns.tolist())

# Step 2️⃣: Count number of employees in each department
dept_count = df["Department"].value_counts()
print("\nEmployee count by department:")
print(dept_count)

# Step 3️⃣: Average Monthly Income by Department
avg_income = df.groupby("Department")["MonthlyIncome"].mean()
print("\nAverage Monthly Income by Department:")
print(avg_income)

# Bar chart for average income
avg_income.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange'])
plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")
plt.show()

# Step 4️⃣: Attrition Analysis (Employees who left vs stayed)
attrition_count = df["Attrition"].value_counts()
print("\nAttrition count:")
print(attrition_count)

# Bar chart for attrition
attrition_count.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Employee Attrition (Yes = Left, No = Stayed)")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.show()

# Step 5️⃣: Compare Average Monthly Income of Employees Who Left vs Stayed
avg_income_attrition = df.groupby("Attrition")["MonthlyIncome"].mean()

print("\nAverage Monthly Income based on Attrition:")
print(avg_income_attrition)

# Visualize it
avg_income_attrition.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Average Monthly Income: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")
plt.show()

# Step 6️⃣: Work-Life Balance vs Attrition
avg_wlb = df.groupby("Attrition")["WorkLifeBalance"].mean()

print("\nAverage Work-Life Balance based on Attrition:")
print(avg_wlb)

# Visualize
avg_wlb.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Work-Life Balance: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Work-Life Balance (1 = Poor, 4 = Excellent)")
plt.show()

# Step 7️⃣: OverTime vs Attrition
overtime_attrition = pd.crosstab(df["OverTime"], df["Attrition"])

print("\nAttrition count based on OverTime:")
print(overtime_attrition)

# Visualize
overtime_attrition.plot(kind='bar', stacked=True, color=['lightgreen', 'tomato'])
plt.title("Attrition based on OverTime")
plt.xlabel("OverTime (Yes = Works Overtime)")
plt.ylabel("Number of Employees")
plt.legend(["Stayed", "Left"])
plt.show()

# Step 8️⃣: Age vs Attrition
avg_age = df.groupby("Attrition")["Age"].mean()
print("\nAverage Age based on Attrition:")
print(avg_age)

avg_age.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Average Age: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Age")
plt.show()

# Step 9️⃣: Summary Report
print("\n--- 📊 Final Summary Report ---")
print(f"1️⃣ Total Employees: {len(df)}")
print(f"2️⃣ Employees Who Left: {attrition_count['Yes']}")
print(f"3️⃣ Attrition Rate: {attrition_count['Yes'] / len(df) * 100:.2f}%")
print(f"4️⃣ Highest Paying Department: {avg_income.idxmax()} ({avg_income.max():.2f})")
print(f"5️⃣ Lowest Paying Department: {avg_income.idxmin()} ({avg_income.min():.2f})")
print(f"6️⃣ Employees Who Left Earned On Avg: ₹{avg_income_attrition['Yes']:.2f}")
print(f"7️⃣ Employees Who Stayed Earned On Avg: ₹{avg_income_attrition['No']:.2f}")
print(f"8️⃣ Avg Work-Life Balance (Left vs Stayed): {avg_wlb['Yes']:.2f} vs {avg_wlb['No']:.2f}")
print(f"9️⃣ Avg Age (Left vs Stayed): {avg_age['Yes']:.2f} vs {avg_age['No']:.2f}")
print("\n✅ Analysis Completed Successfully!")

# --- Step 5: Relationship between Experience and Income ---

import seaborn as sns

print("\nAnalyzing Experience vs. Monthly Income...")

# Scatter plot for YearsAtCompany vs MonthlyIncome
sns.scatterplot(data=df, x="YearsAtCompany", y="MonthlyIncome", hue="Attrition")
plt.title("Years at Company vs Monthly Income (Colored by Attrition)")
plt.xlabel("Years at Company")
plt.ylabel("Monthly Income")
plt.show()
=======
# 📘 Employee Data Analysis Project
# Author: Akash Soni

import pandas as pd
import matplotlib.pyplot as plt

# Step 1️⃣: Load dataset
df = pd.read_csv("employee.csv")

# Show first 5 rows and all column names
print("Here are the first 5 rows of your dataset:")
print(df.head())

print("\nThese are your column names:")
print(df.columns.tolist())

# Step 2️⃣: Count number of employees in each department
dept_count = df["Department"].value_counts()
print("\nEmployee count by department:")
print(dept_count)

# Step 3️⃣: Average Monthly Income by Department
avg_income = df.groupby("Department")["MonthlyIncome"].mean()
print("\nAverage Monthly Income by Department:")
print(avg_income)

# Bar chart for average income
avg_income.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange'])
plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")
plt.show()

# Step 4️⃣: Attrition Analysis (Employees who left vs stayed)
attrition_count = df["Attrition"].value_counts()
print("\nAttrition count:")
print(attrition_count)

# Bar chart for attrition
attrition_count.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Employee Attrition (Yes = Left, No = Stayed)")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.show()

# Step 5️⃣: Compare Average Monthly Income of Employees Who Left vs Stayed
avg_income_attrition = df.groupby("Attrition")["MonthlyIncome"].mean()

print("\nAverage Monthly Income based on Attrition:")
print(avg_income_attrition)

# Visualize it
avg_income_attrition.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Average Monthly Income: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")
plt.show()

# Step 6️⃣: Work-Life Balance vs Attrition
avg_wlb = df.groupby("Attrition")["WorkLifeBalance"].mean()

print("\nAverage Work-Life Balance based on Attrition:")
print(avg_wlb)

# Visualize
avg_wlb.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Work-Life Balance: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Work-Life Balance (1 = Poor, 4 = Excellent)")
plt.show()

# Step 7️⃣: OverTime vs Attrition
overtime_attrition = pd.crosstab(df["OverTime"], df["Attrition"])

print("\nAttrition count based on OverTime:")
print(overtime_attrition)

# Visualize
overtime_attrition.plot(kind='bar', stacked=True, color=['lightgreen', 'tomato'])
plt.title("Attrition based on OverTime")
plt.xlabel("OverTime (Yes = Works Overtime)")
plt.ylabel("Number of Employees")
plt.legend(["Stayed", "Left"])
plt.show()

# Step 8️⃣: Age vs Attrition
avg_age = df.groupby("Attrition")["Age"].mean()
print("\nAverage Age based on Attrition:")
print(avg_age)

avg_age.plot(kind='bar', color=['tomato', 'lightgreen'])
plt.title("Average Age: Employees Who Left vs Stayed")
plt.xlabel("Attrition")
plt.ylabel("Average Age")
plt.show()

# Step 9️⃣: Summary Report
print("\n--- 📊 Final Summary Report ---")
print(f"1️⃣ Total Employees: {len(df)}")
print(f"2️⃣ Employees Who Left: {attrition_count['Yes']}")
print(f"3️⃣ Attrition Rate: {attrition_count['Yes'] / len(df) * 100:.2f}%")
print(f"4️⃣ Highest Paying Department: {avg_income.idxmax()} ({avg_income.max():.2f})")
print(f"5️⃣ Lowest Paying Department: {avg_income.idxmin()} ({avg_income.min():.2f})")
print(f"6️⃣ Employees Who Left Earned On Avg: ₹{avg_income_attrition['Yes']:.2f}")
print(f"7️⃣ Employees Who Stayed Earned On Avg: ₹{avg_income_attrition['No']:.2f}")
print(f"8️⃣ Avg Work-Life Balance (Left vs Stayed): {avg_wlb['Yes']:.2f} vs {avg_wlb['No']:.2f}")
print(f"9️⃣ Avg Age (Left vs Stayed): {avg_age['Yes']:.2f} vs {avg_age['No']:.2f}")
print("\n✅ Analysis Completed Successfully!")

# --- Step 5: Relationship between Experience and Income ---

import seaborn as sns

print("\nAnalyzing Experience vs. Monthly Income...")

# Scatter plot for YearsAtCompany vs MonthlyIncome
sns.scatterplot(data=df, x="YearsAtCompany", y="MonthlyIncome", hue="Attrition")
plt.title("Years at Company vs Monthly Income (Colored by Attrition)")
plt.xlabel("Years at Company")
plt.ylabel("Monthly Income")
plt.show()
>>>>>>> 517bd8387dc02ddc813a7d987429649afd6a734a
