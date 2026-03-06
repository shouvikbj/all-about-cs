from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')
app.secret_key = '2iwudgo8173erbx98ne9udj@$##%^UVbo&%&$&V'


fruits = ["apple", "banana", "cherry", "date", "elderberry"]


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
        return render_template("details.html")
    elif request.method=="POST":
        first_name=request.details.get("first_name")
        last_name=request.details.get("last_name")
        user_dept=request.details.get("user_dept")
        user_colg=request.details.get("user_colg")
        return redirect(f"/details/{first_name}/{last_name}/dept/{user_dept}/college/{user_colg}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)