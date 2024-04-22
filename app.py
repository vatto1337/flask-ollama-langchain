from flask import Flask, request, jsonify
from markupsafe import escape
from classes.llama import LlamaModel

app = Flask("helloWorldApp")


@app.route("/")
def index():
    return "Hello world"

@app.route("/ai", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')

     # Validate the prompt
    if not prompt:
        return jsonify({'error': 'Prompt is missing'}), 400
    
     # Use Llama model to generate text
    model = LlamaModel('llama3')
    generated_text = model.generate_text(prompt)
    
    return jsonify({'generated_text': generated_text})


#  API Error Handling
@app.errorhandler(500)
def handle_500(error):
    return jsonify({'error': 'Internal server error'}), 500