from flask import Flask

app = Flask(__name__)

my_cart = {1: 'Gas' , 2 : 'Super' , 3: 'Diesel'}

@app.route('/')
def index():
    return 'Hello world'


@app.route('/allitems')
def getAllMyItems():
    return my_cart

@app.route('/firstitem')
def onlyFirstItem():
    return my_cart[1]

@app.route('/lastitem')
def justLastItem():
    return my_cart[3]
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')