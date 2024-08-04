import pandas as pd
import pickle #for saving trained model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load dataset
df=pd.read_csv('C:/Users/ompba/ML/Flask-Deployment/Ecommerce Customers.csv')

df.columns
#define features(input) and labels (Output)
features=['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']

label="Yearly Amount Spent"

#extract features and labels
x=df[features]
y=df[label]

#train-test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)

#create linear regression model
Regression_model=LinearRegression()

#train model on training data
Regression_model.fit(x_train,y_train)

#make predictions using trained
print(x_test)
predictions=Regression_model.predict(x_test)

print(predictions)

#save trained model
pickle.dump(Regression_model,open('model.pkl','wb'))