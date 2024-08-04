# Ecommerce Spent Prediction using ML model
## What it is
- Enter the inputs asked in the form
- click on submit
- It will predict result (i.e. yearly amount spent) using our ML model
## Steps followed:
1. Downloaded a dataset Ecommerce csv to create a model on
2. imported required libraries
3. Analysed the data and found it suitable to work with linear regression
4. Model creation:
   - defining features and labels (x,y)
   - split the data in training and test data
   - train the linear regression model using training data
   - prediction on model using test data
5. Then made model.pkl using pickle, to be used in Flask app
6. Creating html page:
   - creating a form with action equals the server url
   - method of form is POST, similar to flask route
   - submit button lets sending input to server
   - response gets printed using {{result}} variable
    
8. Creating Flask App:
   - imported required libraries
   - extract the model from model.pkl using pickle
   - defining /predict route to be called by html
   - converted the data entered by client to dataframe
   - gave the dataframe to model for prediction
   - rendered the result on html page using render_template ]
  
 NOTE: It is the first model I trained and also connected it with client UI, although very basic but for me it's a great start. Will explore and improve my ML knowledge more


 ##Screenshots 
 ![Screenshot (350)](https://github.com/user-attachments/assets/f3909b4d-1d9e-48a9-8590-5bee22500e70)

 ![Screenshot (351)](https://github.com/user-attachments/assets/b8eda727-9067-4460-bafd-6cd4e0eccaf6)
