from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline 

application = Flask(__name__)

app = application

## House for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Gender = request.form.get('Gender'),
            Married = request.form.get('Married'),
            Dependents = request.form.get('Dependents'),
            Education = request.form.get('Education'),
            Self_Employed = request.form.get('Self_Employed'),
            Property_Area = request.form.get('Property_Area'),
            ApplicantIncome = eval(request.form.get('ApplicantIncome')),
            CoapplicantIncome = eval(request.form.get('CoapplicantIncome')),
            LoanAmount = eval(request.form.get('LoanAmount')),
            Loan_Amount_Term = eval(request.form.get('Loan_Amount_Term')),
            Credit_History = eval(request.form.get('Credit_History'))
            )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html',results = results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)