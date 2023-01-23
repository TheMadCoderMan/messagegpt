import requests

# Get the API key
api_key = "YOUR_API_KEY"

for i in range(0, 10000):
    try:
        # Read the dataset
        with open(f"./dataset20/{i}.json", "r", encoding="utf-8") as f:
            dataset = f.read()
    except FileNotFoundError:
        continue

    # Define the fine-tuning parameters
    prompt = (f"Please fine-tune the model using the following dataset:\n{dataset}\n"
              f"After fine-tuning, generate text for the prompt")

    # Make the API request
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 50,
            "top_p": 0.2,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.5,
        },
    )

    # Print the response
    print(response.json())