import pandas as pd
import pickle
from flask import Flask, request,render_template

#creating flask app
app=Flask(__name__)

#Loading model
model=pickle.load(open('model.pkl',"rb"))

@app.route('/')
def check():
    return 'ok'

#define route for predictions
@app.route("/predict",methods=["POST"])
def predict():
    # method must be post to use request
    sl=request.form['sl']
    toa=request.form['toa']
    tow=request.form['tow']
    lom=request.form['lom']

    # converting to dataframe to be sent to model for prediciton
    df=pd.DataFrame({'Avg. Session Length':[sl],'Time on App':[toa],'Time on Website':[tow],'Length of Membership':[lom]})

    prediction=model.predict(df)

    # rendering result on html page
    return render_template('user.html',result=prediction)

#run flask app when this script executed
if __name__=="__main__":
    app.run(debug=True)