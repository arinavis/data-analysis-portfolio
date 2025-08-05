print('________________Working with Files in Python________________')

# Objective: Learn to read and write data from files (CSV, Excel).
# Step 1. I created a list of data in a notepad and saved it as a CSV file in my repository in a separate folder
# Step 2. Reading CSV with Python

# Opening file for reading
with open("data/people.txt", "r", encoding="utf-8") as file:
    # Read lines
    lines = file.readlines()

# Displaying the contents
for line in lines:
    print(line.strip())

