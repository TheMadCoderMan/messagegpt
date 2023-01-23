import json

# Load the large .json file
with open("./dataset19/addition_questions.json", "r") as f:
    data = json.load(f)

# Iterate through each question and answer pair
for i, pair in enumerate(data):
    question = pair["question"]
    answer = pair["answer"]
    
    # Create a dictionary for the current pair
    pair_dict = {"question": question, "answer": answer}
    
    # Save the pair in its own .json file
    with open(f"./dataset20/{i+1}.json", "w") as f:
        json.dump(pair_dict, f)
