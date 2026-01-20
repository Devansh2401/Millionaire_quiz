import os
import random
from flask import Flask, render_template, jsonify, send_from_directory
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase Setup
try:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"CRITICAL: Firebase could not initialize: {e}")

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    all_questions = []
    # Game Logic: 3 easy, 5 medium, 7 hard
    tiers = [('easy', 3), ('medium', 5), ('hard', 7)]
    
    try:
        for difficulty, count in tiers:
            docs = db.collection('questions').where('difficulty', '==', difficulty).stream()
            pool = [d.to_dict() for d in docs]
            
            if len(pool) < count:
                return jsonify({"error": f"Need {count} {difficulty} questions, found {len(pool)}"}), 500
            
            all_questions.extend(random.sample(pool, count))
            
        return jsonify(all_questions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)