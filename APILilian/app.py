#coding=utf-8
#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib


#Initialize the flask App
app = Flask(__name__)
model = joblib.load(open('model.pkl', 'rb'))
scaler = joblib.load('scaler.pkl')
seuil = 0.3   #A définir plus précisément avec le métier


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    #return render_template('index.html', prediction_text= np.array(int_features))
    final_features = scaler.transform([np.array(int_features)])
    #return render_template('index.html', prediction_text= str(final_features) + str(int_features))
    proba = model.predict_proba(final_features)[0][1]
    print(proba)
    if proba > seuil:
        output = "Il faudrait sponsoriser ce joueur"
    else:
        output = "Il ne faudrait pas sponsoriser ce joueur"
    #output = final_features
    return render_template('index.html', prediction_text= output + ", son score est de " + str(round(proba,4)))
    #return render_template('index.html', prediction_text = str(int_features))

if __name__ == "__main__":
    app.run(debug=True)