#!/usr/bin/env python
# coding: utf-8

# In[ ]:


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()
    
    # Convert roll to int
    roll = int(student["roll"])
    
    # Convert marks_str to list of ints
    marks = [int(m) for m in student["marks_str"].split(", ")]
    
    # Validate name (only alphabetic words)
    is_valid = all(word.isalpha() for word in name.split())
    
    if is_valid:
        print(f"{name} ✓ Valid name")
    else:
        print(f"{name} ✗ Invalid name")
    
    # Save cleaned student
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    
    # Print profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

# Find roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nStudent with Roll 103:")
        print(student["name"].upper())
        print(student["name"].lower())


# In[3]:


student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"Student: {student_name}")
print("-----------------------------")

for subject, mark in zip(subjects, marks):

    if 90 <= mark <= 100:
        grade = "A+"
    elif 80 <= mark <= 89:
        grade = "A"
    elif 70 <= mark <= 79:
        grade = "B"
    elif 60 <= mark <= 69:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject} : {mark} : {grade}")


# In[5]:


student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

count = 0

while True:
    subject = input("Enter subject name (or 'done' to stop): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # check numeric input
    if not mark_input.isdigit():
        print("⚠ Invalid input. Marks must be numeric.")
        continue

    mark = int(mark_input)

    # check range
    if mark < 0 or mark > 100:
        print("⚠ Marks must be between 0 and 100.")
        continue

    subjects.append(subject)
    marks.append(mark)
    count += 1
    print("✓ Subject added")

# after loop
updated_average = round(sum(marks) / len(marks), 2)

print("\nNew subjects added :", count)
print("Updated Average    :", updated_average)


# In[4]:


student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Total marks
total = sum(marks)

# Average marks (2 decimal places)
average = round(total / len(marks), 2)

# Highest scoring subject
highest_marks = max(marks)
highest_subject = subjects[marks.index(highest_marks)]

# Lowest scoring subject
lowest_marks = min(marks)
lowest_subject = subjects[marks.index(lowest_marks)]

print(f"Total Marks : {total}")
print(f"Average     : {average}")
print(f"Highest     : {highest_subject} ({highest_marks})")
print(f"Lowest      : {lowest_subject} ({lowest_marks})")


# In[6]:


class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

for name, marks in class_data:
    average = round(sum(marks) / len(marks), 2)

    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    print(f"{name} - Average: {average} - Result: {status}")


# In[7]:


class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    status = "Pass" if avg >= 60 else "Fail"

    print(f"{name:<17} | {avg:>6.2f}  | {status}")


# In[8]:


pass_count = 0
fail_count = 0
averages = []

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)

    if avg >= 60:
        pass_count += 1
    else:
        fail_count += 1

# topper
top_avg = max(averages)
topper = class_data[averages.index(top_avg)][0]

# class average
class_average = round(sum(averages) / len(averages), 2)

print("\nSummary")
print("----------------------------")
print(f"Passed Students : {pass_count}")
print(f"Failed Students : {fail_count}")
print(f"Class Topper    : {topper} ({top_avg})")
print(f"Class Average   : {class_average}")


# In[9]:


essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: strip whitespace
clean_essay = essay.strip()

print("Step 1 - Stripped Essay:")
print(clean_essay)


# In[11]:


# Step 2: Convert to Title Case
title_case = clean_essay.title()

print("\nStep 2 - Title Case:")
print(title_case)


# In[12]:


# Step 3: Count occurrences of "python"
count_python = clean_essay.count("python")

print("\nStep 3 - 'python' count:")
print(count_python)


# In[13]:


# Step 4: Replace "python" with "Python 🐍"
replaced_essay = clean_essay.replace("python", "Python 🐍")

print("\nStep 4 - Replaced Essay:")
print(replaced_essay)


# In[14]:


# Step 5: Split into sentences
sentences = clean_essay.split(". ")

print("\nStep 5 - Sentences List:")
print(sentences)


# In[15]:


# Step 6: Print numbered sentences
print("\nStep 6 - Numbered Sentences:")

for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()
    
    if not sentence.endswith("."):
        sentence += "."
        
    print(f"{i}. {sentence}")

