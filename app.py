from flask import Flask, request, jsonify
from detoxify import Detoxify

app = Flask(__name__)
detoxify_model = Detoxify('original')

# Replace this with your API key
API_KEY = 'your-api-key'

@app.route('/detoxify', methods=['POST'])
def detoxify_text():
    api_key = request.headers.get('API-Key')
    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401
    text = request.json['text']
    model_res = detoxify_model.predict(text)
    return jsonify(str(model_res))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
