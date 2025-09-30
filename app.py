from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = 'your-openai-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
