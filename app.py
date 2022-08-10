import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
decision_tree_model = pickle.load(open('decision_tree-model.pkl','rb'))
knn_model = pickle.load(open('knn-model.pkl','rb'))
random_forest_model = pickle.load(open('random_forest-model.pkl','rb'))
naive_bayes_model = pickle.load(open('naive_bayes-model.pkl','rb'))
svm_model = pickle.load(open('svm-model.pkl','rb'))


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])

def predict():

    CreditScore = float(request.args.get('CreditScore'))
    Age = float(request.args.get('Age'))
    Tenure = float(request.args.get('Tenure'))
    Balance = float(request.args.get('Balance'))
    NumOfProducts = float(request.args.get('NumOfProducts'))
    EstimatedSalary = float(request.args.get('EstimatedSalary'))
    Geography = (request.args.get('Geography'))

    if Geography=="France":
      Geography = 0
    elif Geography=="Spain":
      Geography = 1
    else:
      Geography = 2

    Gender = (request.args.get('Gender'))

    if Gender=="Male":
      Gender = 1
    else:
      Gender= 0

    HasCrCard = (request.args.get('HasCrCard'))

    if HasCrCard=="Yes":
      HasCrCard = 1
    else:
      HasCrCard = 0

    IsActiveMember = (request.args.get('IsActiveMember'))

    if IsActiveMember=="Yes":
      IsActiveMember = 1
    else:
      IsActiveMember = 0
   
    Model = (request.args.get('Model'))

    if Model=="Decision Tree Algorithm":
      prediction = decision_tree_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    elif Model=="Decision Tree Algotihm":
      prediction = knn_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    elif Model=="Random Forest Algorithm":
      prediction = random_forest_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    elif Model=="Naive Bayes Algotihm":
      prediction = naive_bayes_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    else:
      prediction = svm_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

    
    if prediction == [0]:
      return render_template('index.html', prediction_text='The Person is exited')
    
    else:
      return render_template('index.html', prediction_text='The person not exited yet')


if __name__=="__main__":
    app.run(debug=True)