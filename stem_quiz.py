
print("=" * 35)
print("       AI & STEM QUIZ")
print("=" * 35)

questions = [
    {
        "question": "1. What does AI stand for?",
        "options": [
            "A. Automated Internet",
            "B. Artificial Intelligence",
            "C. Advanced Information"
        ],
        "answer": "B"
    },
    {
        "question": "2. What is 12 squared?",
        "options": [
            "A. 24",
            "B. 124",
            "C. 144"
        ],
        "answer": "C"
    },
    {
        "question": "3. Which language is used in this project?",
        "options": [
            "A. Python",
            "B. HTML",
            "C. CSS"
        ],
        "answer": "A"
    },
    {
        "question": "4. Which unit measures force?",
        "options": [
            "A. Watt",
            "B. Newton",
            "C. Volt"
        ],
        "answer": "B"
    },
    {
        "question": "5. What is a main goal of AI?",
        "options": [
            "A. Help solve problems",
            "B. Replace all mathematics",
            "C. Stop computers working"
        ],
        "answer": "A"
    }
]

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer (A, B, or C): ")
    answer = answer.strip().upper()

    if answer == question["answer"]:
        print("Correct! Well done.")
        score += 1
    else:
        print("Not quite. The correct answer is",
              question["answer"])

print("\n" + "=" * 35)
print("QUIZ COMPLETE!")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent work!")
elif score >= 3:
    print("Good job! Keep learning.")
else:
    print("Keep practising. You can improve!")

print("=" * 35)
