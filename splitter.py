import json

# Read the .json file
with open("./dataset18/simplified-nq-train.jsonl", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract the text from the json file
text = "\n".join(data[""])

# Split the data into chunks of 1024 tokens or less
chunk_size = 1024
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Write the chunks to separate .json files
for i, chunk in enumerate(chunks):
    # create a new dictionary
    new_data = {"positive":chunk} 
    with open(f"./dataset20/captain-knowledge-{i}.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f)