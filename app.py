import os
import random
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
    fb_config = os.environ.get('FIREBASE_CONFIG') 
    if fb_config:
        cred = credentials.Certificate(json.loads(fb_config))
    else:
        raise ValueError("No FIREBASE_CONFIG found in environment variables!")

firebase_admin.initialize_app(cred)
db = firestore.client()

# --- ROUTES ---

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """Serves images, logos, and other assets."""
    return send_from_directory('assets', filename)

@app.route('/')
def index():
    """Serves the main game interface."""
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    """
    Fetches questions from Firestore.
    Logic: 3 Easy, 5 Medium, 7 Hard (Total 15).
    Includes double-shuffle to prevent repetition from the 150-question pool.
    """
    all_game_questions = []
    # Difficulty tiers and the count required for a full game
    tiers = [('easy', 3), ('medium', 5), ('hard', 7)]
    
    try:
        for difficulty, count in tiers:
            # 1. Fetch all questions matching the difficulty
            docs = db.collection('questions').where('difficulty', '==', difficulty).stream()
            pool = [d.to_dict() for d in docs]
            
            # 2. Safety check: Ensure the database has enough questions
            if len(pool) < count:
                return jsonify({
                    "error": f"Insufficient {difficulty} questions. Need {count}, found {len(pool)}."
                }), 500
            
            # 3. Strategy: First shuffle the entire pool of 150
            random.shuffle(pool)
            
            # 4. Then pick 'count' unique questions from that shuffled pool
            selection = random.sample(pool, count)
            
            # 5. Add them to the final game set
            all_game_questions.extend(selection)
            
        # Optional: If you want the questions within the game to be mixed 
        # (e.g., not always start with 3 easy ones), uncomment the line below:
        # random.shuffle(all_game_questions)
        
        return jsonify(all_game_questions)

    except Exception as e:
        # Catch-all for database connection issues or logic errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use the port Render provides (PORT environment variable)
    # Default to 5000 for local development on your Mac
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)