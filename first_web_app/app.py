from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = '2iwudgo8173erbx98ne9udj@$##%^UVbo&%&$&V'


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Load the trained ML model at the start of the application
loaded_model = pickle.load(open("./static/models/diabetes_model.pkl","rb"))
loaded_scaler = pickle.load(open("./static/models/scaler.pkl","rb"))


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/anasmita')
def anasmita():
    return render_template('anasmita.html')

@app.route('/<first_name>/<last_name>')
def dynamic_greeting(first_name, last_name):
    return render_template(
        'dynamic.html', 
        first_n=first_name.capitalize(), 
        last_n=last_name.capitalize(),
        fruits=fruits
    )

@app.route('/user/<email>')
def dynamic_with_age(email):
    return render_template(
        'dynamic.html', 
        u_email=email,
        fruits=fruits
    )

@app.route('/details/<first_name>/<last_name>/dept/<dept_name>/college/<college_name>')
def details(first_name,last_name,dept_name,college_name):
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    cap_fruits = [fruit.capitalize() for fruit in fruits]
    return render_template(
        'details.html',
        first_n=first_name.capitalize(), 
        last_n=last_name.capitalize(),
        dept_n=dept_name.upper(),
        college_n=college_name.upper(),
        fruits=cap_fruits
    )

# Types of requests in HTTP
"""
    GET: Get data from Database using server
    POST: Create new entry into Database using server
    UPDATE: Update existing entry into Database using server
    PUT: Update part of existing entry into Database using server
    DELETE: Delete existing entry from Database using server
"""

# TODO:
"""
1. if email id is available, must redirect user to the proper email based route.
2. else redirect user to name base route
3. print password in each case
"""
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        user_password = request.form.get("user_password")
        user_email=request.form.get("user_email")
        print(f"Password: {user_password}")
        if user_email:
            return redirect(f"/user/{user_email}")
        else:
            return redirect(f"/{first_name}/{last_name}")
    else:
        return "Requested method not allowed!"

@app.route('/student',methods=["GET","POST"])
def student():
    if request.method=="GET":
        return render_template("student.html")
    elif request.method=="POST":
        first_name=request.form.get("first_name")
        last_name=request.form.get("last_name")
        user_department=request.form.get("user_department")
        user_college=request.form.get("user_college")
        return redirect(f"/details/{first_name}/{last_name}/dept/{user_department}/college/{user_college}")

@app.route('/predict')
def predict():
    return render_template("predict.html")

# API endpoint for prediction
@app.route('/predict/diabetes', methods=["POST"])
def predict_diabetes():
    pregnancies = float(request.form.get("pregnancies"))
    glucose = float(request.form.get("glucose"))
    blood_pressure = float(request.form.get("blood_pressure"))
    skin_thickness = float(request.form.get("skin_thickness"))
    insulin = float(request.form.get("insulin"))
    bmi = float(request.form.get("bmi"))
    dpf = float(request.form.get("dpf"))
    age = float(request.form.get("age"))
    # Feature Names 
    feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    input_data = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]
    # Prediction using the loaded model
    input_df = pd.DataFrame([input_data], columns=feature_names)
    scaled_input = loaded_scaler.transform(input_df)
    prediction = loaded_model.predict(scaled_input)
    if prediction[0] == 1:
        result = "The model predicts that you have diabetes."
    else:
        result = "The model predicts that you don't have diabetes."
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)