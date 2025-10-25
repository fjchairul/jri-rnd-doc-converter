# Create the WebPage for UI using React

## 1. **Install Homebrew (if you don't have it)**

Open the Terminal app (find it via Spotlight Search).

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. Install Pandoc

In Terminal, run:

```
brew install pandoc
```

This will download and install Pandoc on your Mac.​

## 3. Install Python 3 (if not installed)

macOS may already have Python 3, but you can make sure with:

```
brew install python
```

Check it’s installed:

```
python3 --version
```

## 4. Set Up a Python Virtual Environment

In Terminal, go to your project folder, or create one:

```
mkdir myproject
cd myproject
python3 -m venv venv
```


Activate the virtual environment:

```
source venv/bin/activate
```

## 5. Install Flask

With your virtual environment activated, install Flask:

```
pip install Flask
```

This sets up Flask for developing your web server.​

## 6. Install Node.js and npm
Node.js is required to run React.
Download and run the macOS installer here: https://nodejs.org/en/download
Or use Homebrew:

```
brew install node
```

Check installations:

```
node -v
npm -v
```

## 7. Create a React App
In a different folder, run:

```
npx create-react-app jri-helper-doc-md
cd jri-helper-doc-md
npm start
```

This starts your React app locally so you can develop your UI.​

## 8. (Optional) Install React Markdown Renderer
Inside your React app folder, run:

```
npm install react-markdown
```

This will make it easier to display markdown content.

## 9. Install Bootstrap in your React App
Run this command inside your React project folder:

```
npm install bootstrap
```

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