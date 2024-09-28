from flask import Flask,render_template,request,redirect,url_for
import json
import joblib
import numpy as np

app = Flask(__name__)

    # uploading json file and trained model
try:
    with open('flight_columns.json','r') as f:
        data = json.load(f)
    model = joblib.load('flight_price_prediction_model.joblib')
except:
    import sys
    print('Some error occured')
    sys.exit()    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST','GET'])
def process():


    # Initialize array of size 30 with default values of 0 for prediction
    arr = [0] * 30
    # Get form data
    flight_class = request.form.get('class')  # 'Economy' or 'Business'
    duration = float(request.form.get('duration', 0))  # Convert to float, default 0
    days_left = float(request.form.get('days_left', 0))  # Convert to float, default 0
    airline = request.form.get('airline')  # Airline name
    source_city = request.form.get('source_city')
    departure_time = request.form.get('departure_time')
    stops = request.form.get('stops')
    arrival_time = request.form.get('arrival_time')
    destination_city = request.form.get('destination_city')
    

    # Class: Business --1 economy --0
    if flight_class=='Business':
        arr[0]=1
        #default 0 is for economy

    # duration and days left with same values given by user
    arr[1] = duration
    arr[2] = days_left

    # Set 3rd index to 1 if airline is 'Air_India' and so on
    if airline in data['data_columns']:
        index=-1
        index = data['data_columns'].index(airline)
        if index>0:
            arr[index]=1
    if source_city in data['data_columns']:
        index=-1
        index = data['data_columns'].index(source_city)
        if index>0:
            arr[index]=1
    if departure_time in data['data_columns']:
        index=-1
        index = data['data_columns'].index(departure_time)
        if index>0:
            arr[index]=1
    if stops in data['data_columns']:
        index=-1
        index = data['data_columns'].index(stops)
        if index>0:
            arr[index]=1
    if arrival_time in data['data_columns']:
        index=-1
        index = data['data_columns'].index(arrival_time)
        if index>0:
            arr[index]=1
    if destination_city in data['data_columns']:
        index=-1
        index = data['data_columns'].index(destination_city)
        if index>0:
            arr[index]=1
        
    return redirect(url_for('predict',arr=arr))


@app.route('/predict',methods=['POST','GET'])
def predict():
    arr = request.args.getlist('arr',type=float)
    arr = np.array(arr).reshape(1,-1)
    prediction = model.predict(arr)
    return render_template('predict.html',prediction=prediction[0])

@app.route('/reset')
def reset():
    global input_values
    input_values = []  # Reset input values
    return render_template('index.html')  # Render the input form
    
    

if __name__=='__main__':
    app.run(debug=True)