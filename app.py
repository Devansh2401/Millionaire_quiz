import os
import random  # This is the missing line!

# ... rest of your imports
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)

# --- SECURE FIREBASE CONNECTION ---
if os.path.exists("firebase_key.json"):
    # Local development (Mac)
    cred = credentials.Certificate("firebase_key.json")
else:
    # Production (Render)
    # STEP 1: Define the variable first!
    fb_config = os.environ.get('FIREBASE_CONFIG') 
    
    # STEP 2: Now you can check if it exists
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
    # Use the port Render provides, or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)