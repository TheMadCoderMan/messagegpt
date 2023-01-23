from flask import Flask, render_template, request
import json
import requests

def preprocess_input(user_input):
    # Strip out any extra characters or whitespace from the input
    user_input = user_input.strip()
    return user_input

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_input = preprocess_input(user_input)
        headers = {
            'Content-Type': 'application/json', 
            'Authorization': 'Bearer YOUR_API_KEY'
        }
        data = json.dumps({
            "prompt": user_input,
            "max_tokens": 1024
        })
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)
        if response.ok:
            response_text = response.json()['choices'][0]['text']
        else:
            return "An error occurred: {}".format(response.text)
        return render_template('index.html', response_text=response_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
