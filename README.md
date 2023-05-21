# hackathon
Our project for *JacobsHack! 2022*, "Carbon Trainer", aims to show the possible carbon savings of a railway between two cities by estimating the construction costs and replaced automotive traffic.  

This code is mostly functional, but there were a few bugs that we didn't have time to sort out by the submission deadline.  

# Quick start

### Backend

1. `cd ./backend`  
2. `python -m venv venv`  
3. `source venv/Scripts/activate` (or `./venv/Scripts/activate.bat` on Windows)  
4. `pip install -r requirements.txt`  
5. `python server.py`  

You should now be able to connect to the backend server (http://localhost:8000/docs).

### Frontend

1. `cd ./frontend`  
2. `npm install`  
3. `npm start`  

You should now be able to connect to the frontend server (http://localhost:3000/). The backend must be running for any special content to be rendered. 

