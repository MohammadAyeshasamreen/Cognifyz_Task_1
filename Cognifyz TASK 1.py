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