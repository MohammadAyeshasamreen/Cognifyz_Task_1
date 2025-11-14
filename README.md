# ✅ **📌Task 1 Project Submission: Text-Based Quiz Game**

## **1. Project Title**

**Simple Text-Based Quiz Game Using Conditional Statements**

---

## **2. Objective**

The objective of this project is to develop a basic **text-based quiz game** using **conditional statements** to control game logic and flow.
This fulfills the requirements of Level 1 (Beginner) – Task 1.

---

## **3. Project Description**

This project implements a simple interactive quiz game in Python.
The player will be asked multiple questions, and based on their responses, the game will evaluate answers using **if-else conditional statements**.

The game keeps track of the player’s score and displays the final result at the end.

---

## **4. Steps Followed (As Required)**

### ✔ **1. Selected Game Type**

Quiz Game

### ✔ **2. Defined Rules**

* The game asks 5 general-knowledge questions.
* Each correct answer gives 1 point.
* Answers are case-insensitive.
* At the end, the total score is displayed.

### ✔ **3. Used Conditional Statements**

The game checks each answer with `if / else` logic.

### ✔ **4. Tested & Debugged**

The program runs correctly in Python without errors.

---

## **5. Complete Python Code (Well-Commented)**

```python
# Quiz Game - Text-Based Game using Conditional Statements

print("🎉 Welcome to the Quiz Game! 🎉")
print("Answer the following questions:\n")

score = 0   # To store total score

# Question 1
answer = input("1. What is the capital of India? ").strip().lower()
if answer == "delhi":
    print("✔ Correct!\n")
    score += 1
else:
    print("✘ Wrong! The correct answer is Delhi.\n")

# Question 2
answer = input("2. How many days are there in a week? ").strip()
if answer == "7":
    print("✔ Correct!\n")
    score += 1
else:
    print("✘ Wrong! The correct answer is 7.\n")

# Question 3
answer = input("3. Who is known as the Father of Computers? ").strip().lower()
if answer == "charles babbage" or answer == "babbage":
    print("✔ Correct!\n")
    score += 1
else:
    print("✘ Wrong! The correct answer is Charles Babbage.\n")

# Question 4
answer = input("4. Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("✔ Correct!\n")
    score += 1
else:
    print("✘ Wrong! The correct answer is Mars.\n")

# Question 5
answer = input("5. How many continents are there in the world? ").strip()
if answer == "7":
    print("✔ Correct!\n")
    score += 1
else:
    print("✘ Wrong! The correct answer is 7.\n")

# Final Score
print("🎯 Quiz Completed!")
print(f"Your Final Score: {score}/5")

# Performance message
if score == 5:
    print("🏆 Excellent! You're a genius!")
elif score >= 3:
    print("👍 Good job! Keep learning.")
else:
    print("📘 Keep practicing! You'll improve.")
```

---

## **6. Sample Output**

```
🎉 Welcome to the Quiz Game! 🎉
Answer the following questions:

1. What is the capital of India? delhi
✔ Correct!

2. How many days are there in a week? 7
✔ Correct!

3. Who is known as the Father of Computers? charles babbage
✔ Correct!

4. Which planet is known as the Red Planet? mars
✔ Correct!

5. How many continents are there in the world? 7
✔ Correct!

🎯 Quiz Completed!
Your Final Score: 5/5
🏆 Excellent! You're a genius!
```

---

## **7. Conclusion**

This project demonstrates how to create a simple text-based quiz game using **conditional statements** to control game logic.
It shows essential programming concepts like:

* User input handling
* String processing
* Conditional decision-making
* Score calculation

This fulfills all requirements of the **Beginner Level Task 1**.
