import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000],
    'Department': ['HR', 'IT', 'Finance', 'IT']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic operations
print("\nDataFrame Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

# Filter data
print("\nIT Department employees:")
print(df[df['Department'] == 'IT'])

# Group by Department
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

# Sort by Salary
print("\nSorted by Salary:")
print(df.sort_values('Salary', ascending=False))