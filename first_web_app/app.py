from flask import Flask, render_template

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
    # TODO: provide your implementation
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)