import json

questions = []
for i in range(1, 101):
    for j in range(1, 101):
        question = {"question": f"What is {i}+{j}?", "answer": f"{i}+{j} = {i+j}"}
        questions.append(question)

with open("./dataset19/addition_questions.json", "w") as f:
    json.dump(questions, f)
