# Backend for Upload API

## 1. Set up your Flask project
Inside your project folder (not the React folder), open Terminal and create a new directory:

```
mkdir backend
cd backend
```

Then, activate your Python virtual environment (if not already activated):
```
source ../venv/bin/activate
```

## 2. Install dependencies
Install Flask and pypandoc:

```
pip install Flask pypandoc python-dotenv
```

## 3. Create your Flask app
Create a new file named app.py inside the backend folder and add this code ...
This Flask app:
Accepts files sent via POST.
Saves the file temporarily.
Converts it with Pandoc to Markdown using pypandoc.
Returns the Markdown as JSON.

## 4. Enable CORS in Flask
Make sure you have installed Flask-CORS:

```
pip install flask-cors
```

## 5. Run your Flask backend
In Terminal inside backend:

```
flask run
```
You should see something like:

`Running on http://127.0.0.1:5000`

## 6. Connect your React frontend to Flask
Your frontend is already set up to send requests to http://localhost:5000/upload, so now it should work automatically.

## 7. To test:
```
curl -X POST -F ""file=@Business Requirements Document (BRD).docx"" http://127.0.0.1:5000/upload
```

Run your Flask backend 

```
flask run
```

In another Terminal window, start your React app 

```
npm start
```

Upload a .docx or .pdf file on your webpage.
The converted Markdown should appear in the text area.