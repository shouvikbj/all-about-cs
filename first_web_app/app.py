from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
app.secret_key = '2iwudgo8173erbx98ne9udj@$##%^UVbo&%&$&V'


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)