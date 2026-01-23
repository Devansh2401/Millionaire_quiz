import os
import random
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)

if os.path.exists("firebase_key.json"):
    cred = credentials.Certificate("firebase_key.json")
else:
    fb_config = os.environ.get('FIREBASE_CONFIG') 
    if fb_config:
        cred = credentials.Certificate(json.loads(fb_config))
    else:
        raise ValueError("No FIREBASE_CONFIG found in environment variables!")

firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    all_game_questions = []
    tiers = [('easy', 3), ('medium', 5), ('hard', 7)]
    
    try:
        for difficulty, count in tiers:
            docs = db.collection('questions').where('difficulty', '==', difficulty).stream()
            pool = [d.to_dict() for d in docs]
            
            if len(pool) < count:
                return jsonify({"error": f"Insufficient {difficulty} questions."}), 500
            
            random.shuffle(pool)
            selection = random.sample(pool, count)
            all_game_questions.extend(selection)
        
        return jsonify(all_game_questions)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)