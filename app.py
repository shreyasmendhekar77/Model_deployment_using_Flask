import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
Reg_model=pickle.load(open('Regression_model.pkl','rb'))
scalar=pickle.load(open('scaler_standardization.pkl','rb'))
# It is a kind of HOME page
@app.route('/')
def home():
    return render_template('home.html')

# This predict.api along with POST method is used to predict the output
@app.route('/predict.api',methods=['POST'])
def predict_api():
    data=request.json['data'] # Getting the data from the user
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    # now standardizing the new data
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=Reg_model.predict(new_data)
    print(output[0])
    return jsonify({'output':output[0]})

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=Reg_model.predict(final_input)[0]
    return render_template('home.html',prediction_text='The House price prediction is {}'.format(output))


if __name__ == '__main__':  
    app.run(debug=True)
