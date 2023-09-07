import random

score = 0
num1 = random.randint(0, 1)
num2 = random.randint(0, 1)

print("Day 1:", num1)
print("Day 2:", num2)

if num1 == 1:
    score += 1

if num2 == 1:
    score += 1

score = min(1, score)  # Ensure score is not more than 1

print("Final Score:", score)

# Provide a description based on the score
if score == 0:
    print("The stock market is not doing so well.")
elif score == 1:
    print("The stock market is doing well!")
