from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML file
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    # Get the age from the JSON request
    data = request.json
    try:
        enter_age = int(data.get('age'))
        your_age = random.randint(1, 10)
        
        if enter_age == your_age:
            return jsonify({"success": True, "message": f"Access Granted ✅ (System: {your_age})"})
        else:
            return jsonify({"success": False, "message": f"Try again! ❌"})
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Please enter a valid number"}), 400

if __name__ == '__main__':
    app.run(debug=True)