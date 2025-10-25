#!/bin/bash
cd backend
source ../venv/bin/activate
python app.py &
cd ../jri-helper-doc-md
npm start


#./run.sh to run