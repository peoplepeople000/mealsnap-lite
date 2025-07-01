from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import base64
import sqlite3

app = Flask(__name__)
CORS(app)

# Load .env variables
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/nateraw/food"
HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
    "Content-Type": "application/json"
}

# ✅ Query calories from SQLite DB
def get_calories_from_db(food_name):
    try:
        # Standardize: lowercase + replace spaces with underscores
        clean_name = food_name.lower().replace(" ", "_")
        conn = sqlite3.connect('calories.db')
        cursor = conn.cursor()
        cursor.execute("SELECT calories FROM food_calories WHERE food = ?", (clean_name,))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else 100
    except Exception as e:
        print(f"DB Error: {str(e)}")
        return 100

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        image_bytes = request.files['image'].read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")

        payload = {"inputs": encoded_image}
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        hf_result = response.json()

        print("HF Response:", hf_result)

        top_result = hf_result[0]
        label = top_result['label']
        confidence = top_result['score']

        # ✅ Use SQLite to get calories
        calories = get_calories_from_db(label)
        print("Label:", label)
        print("Calories:", calories)

        result = {
            "food": label,
            "confidence": confidence,
            "calories": calories,
            "message": f"Predicted {label} with confidence {confidence:.2f}"
        }

        return jsonify(result)

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
