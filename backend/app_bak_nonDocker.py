from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pypandoc

app = Flask(__name__)
CORS(app)   
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        output = pypandoc.convert_file(filepath, "md")
        return jsonify({"markdown": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
    print("Flask server started.")