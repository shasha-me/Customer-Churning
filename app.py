from flask import Flask, render_template,request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


#we have imported the made model
app = Flask(__name__)
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

#now we need to directly name our web

@app.route('/', methods =['GET'])
def Home():
    return render_template('index.html')

#standardizing values

standard_to = StandardScaler()
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input data from the form
    CreditScore = int(request.form['CreditScore'])

    Age = int(request.form['Age'])
    Tenure = int(request.form['Tenure'])
    Balance = float(request.form['Balance'])
    NumOfProducts = int(request.form['NumOfProducts'])
    HasCrCard = int(request.form['HasCrCard'])
    IsActiveMember = int(request.form['IsActiveMember'])
    EstimatedSalary = float(request.form['EstimatedSalary'])
    SatisfactionScore = int(request.form['SatisfactionScore'])
    PointEarned = int(request.form['PointEarned'])

    Geography_Germany = request.form['Geography_Germany']
    if (Geography_Germany == 'Germany'):
        Geography_Germany = 1
        Geography_Spain = 0
        Geography_France = 0

    elif (Geography_Germany == 'Spain'):
        Geography_Germany = 0
        Geography_Spain = 1
        Geography_France = 0

    else:
        Geography_Germany = 0
        Geography_Spain = 0
        Geography_France = 1

    Gender_Male = request.form['Gender_Male']
    if (Gender_Male == 'Male'):
        Gender_Male = 1
        Gender_Female = 0
    else:
        Gender_Male = 0
        Gender_Female = 1

    CardType_DIAMOND = request.form['CardType_DIAMOND']
    if (CardType_DIAMOND == 'DIAMOND'):
        CardType_DIAMOND = 1
        CardType_GOLD = 0
        CardType_PLATINUM = 0
        CardType_SILVER = 0

    elif (CardType_DIAMOND == 'GOLD'):
        CardType_DIAMOND = 0
        CardType_GOLD = 1
        CardType_PLATINUM = 0
        CardType_SILVER = 0
    elif (CardType_DIAMOND == 'SILVER'):
        CardType_DIAMOND = 0
        CardType_GOLD = 0
        CardType_PLATINUM = 0
        CardType_SILVER = 1
    else:
        CardType_DIAMOND = 0
        CardType_GOLD = 0
        CardType_PLATINUM = 1
        CardType_SILVER = 0


    prediction = model.predict([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard,IsActiveMember, EstimatedSalary, SatisfactionScore,PointEarned, Geography_Germany, Geography_Spain,
       Gender_Male, CardType_GOLD, CardType_PLATINUM,
       CardType_SILVER]])
    if prediction == 1:
        return render_template('index.html', prediction_text="The Customer will leave the bank")
    else:
        return render_template('index.html', prediction_text="The Customer will not leave the bank")

if __name__ == '__main__':
    app.run(debug=True)