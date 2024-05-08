#libraries
import fastapi as fastapi
import numpy as np
import pandas as pd
import uvicorn
import pickle
import BankNotes as bn

#create thethe app object
app = fastapi()
pickle_in = open("Classifier.pkl", "rb")
Classifier = pickle.load(pickle_in)

#Index page
@app.get('/')
def index():
    return { 'message' : 'Hello, Asma'}