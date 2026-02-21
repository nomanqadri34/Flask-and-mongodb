from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from pymongo import MongoClient
from datetime import datetime
import traceback

app = Flask(__name__)

# MongoDB Atlas connection
MONGODB_URI = "mongodb+srv://nomanqadri34:U0hSWV1mHsiR7PJo@cluster1.xhpp5nd.mongodb.net/new1"

def get_mongo_client():
    """Create and return MongoDB client"""
    try:
        client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        # Verify connection
        client.admin.command('ping')
        return client
    except Exception as e:
        print(f"MongoDB Connection Error: {e}")
        return None

# Route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# API route to get products from JSON file
@app.route('/api')
def get_api():
    try:
        # Get the data directory path
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'products.json')
        
        # Read from the backend file
        with open(data_file, 'r') as f:
            data = json.load(f)
        
        # Return JSON response
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Get form data
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'message': request.form.get('message'),
            'submitted_at': datetime.now().isoformat()
        }
        
        # Validate required fields
        if not data['name'] or not data['email'] or not data['phone']:
            return render_template('index.html', 
                                 error="Name, Email, and Phone are required fields.")
        
        # Connect to MongoDB
        client = get_mongo_client()
        if not client:
            return render_template('index.html', 
                                 error="Database connection failed. Please try again later.")
        
        # Insert data into MongoDB
        try:
            db = client['new1']
            collection = db['submissions']
            result = collection.insert_one(data)
            client.close()
            
            # Redirect to success page
            return redirect(url_for('success'))
        except Exception as db_error:
            client.close()
            error_msg = f"Failed to insert data: {str(db_error)}"
            return render_template('index.html', error=error_msg)
    
    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        return render_template('index.html', error=error_msg)

# Route to display success message
@app.route('/success')
def success():
    return render_template('success.html')

# Route to get all submissions (for viewing data)
@app.route('/submissions')
def get_submissions():
    try:
        client = get_mongo_client()
        if not client:
            return jsonify({"error": "Database connection failed"}), 500
        
        db = client['new1']
        collection = db['submissions']
        submissions = list(collection.find({}, {'_id': 0}))
        client.close()
        
        return jsonify(submissions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
