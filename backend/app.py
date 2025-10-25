from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pypandoc

app = Flask(__name__, static_folder='../jri-helper-doc-md/build')
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
        # Convert file to markdown
        output = pypandoc.convert_file(filepath, "md")
        
        # Delete the uploaded file after conversion
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify({"markdown": output})
    except Exception as e:
        # Clean up file even if conversion fails
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({"error": str(e)}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
