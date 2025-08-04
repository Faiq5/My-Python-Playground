questions = [{"question": "What is the capital of France?","answer": "paris"},
            {"question": "What is the largest mammal?", "answer": "blue whale"},
            {"question": "What is the smallest prime number?", "answer": "2"},
            {"question": "What is the main ingredient in guacamole?", "answer": "avocado"},
            {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"}]

score = []
asked = []
import random
random.shuffle(questions)
print("Welcome to the Quiz App!")
print("Type 'exit' to quit at any time.")

for q in questions:
    asked.append(q["question"])
    answer = input(q["question"] + " ")
    if answer.lower() == "exit":
        print("Exiting the Quiz App. Goodbye!")
        break
    if answer.lower() == q["answer"].lower():
        print("Correct!")
        score.append(1)
    else:
        print("Incorrect. The correct answer is:", q["answer"])

print("Your total score is:", sum(score)/len(questions) * 100, "%")