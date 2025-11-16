# Day 37 — Length Converter GUI App Using Tkinter

This project is a part of my **#100DaysLearningChallenge**.  
Today’s goal was to revise Tkinter basics and build a **mini Length Converter application** that converts values between meters, centimeters, feet, and inches.

This small GUI project helped strengthen concepts like:
- Tkinter window management  
- Entry widgets for user input  
- Combobox for unit selection  
- Buttons and events  
- StringVar usage  
- Updating label content dynamically  
- Creating real interactive desktop apps in Python  

---

## 🧠 What is Tkinter?

**Tkinter is the standard GUI (Graphical User Interface) library in Python.**  
It allows you to create desktop applications using simple Python code.

### ✔ Key reasons why Tkinter is useful:
- Comes built-in with Python (no installation needed)
- Beginner-friendly for learning GUI programming
- Supports widgets like:
  - Entry  
  - Button  
  - Label  
  - Combobox  
  - Treeview  
  - Frames  
- Perfect for making quick tools, utilities, and educational apps
- Follows **event-driven programming** (button click → action happens)

---

## 📏 About This Project — Length Converter App

In this mini-project, the app:
- Takes a number from the user (via `Entry`)
- Lets the user choose a unit (meters, centimeters, feet, inches)
- Converts that value into all four units
- Displays the final result in the GUI

This is the type of app you often see in:
- Unit converter tools  
- Engineering calculators  
- Educational GUI utilities  
- Desktop-based utility apps  

---

## 🔧 How It Works (Concept Explanation)

### 1️⃣ Getting user input  
We use an **Entry widget** to take a numeric input.

### 2️⃣ Selecting a unit  
We use a **Combobox** with a `StringVar` to store the selected unit.

### 3️⃣ Converting values  
The logic is handled in a simple function:

```python
def convert_length(value, unit):
