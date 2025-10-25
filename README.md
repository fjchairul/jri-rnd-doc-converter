# Preparing for Docker

## 1. Prepare React frontend
Go to React app folder (jri-helper-doc-md)
Install dependencies:

```
npm install
```

Build production assets:

```
npm run build
```

## 2. Create backend/requirements.txt
List Python dependencies:
```
Flask
flask-cors
pypandoc
```

## 3. Create Dockerfile in project root (where backend and frontend directory are)
Sample Dockerfile:

```
FROM python:3.10-slim

WORKDIR /app

COPY backend backend
COPY jri-helper-doc-md/build jri-helper-doc-md/build
COPY backend/requirements.txt backend/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt && \
    pip install pypandoc flask-cors

RUN apt-get update && apt-get install -y pandoc && apt-get clean

EXPOSE 5000

CMD [""python"", ""backend/app.py""]
```

## 4. Build Docker image locally
Run in terminal:

```
docker build -t jrihelper-app .
```

Make sure Docker daemon is running.

## 5. Run Docker container locally
```
docker run -p 5000:5000 jrihelper-app
```

Open browser at http://localhost:5000 to access the app.
