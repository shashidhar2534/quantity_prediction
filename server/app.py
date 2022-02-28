from flask import Flask, redirect, url_for, render_template, request, jsonify
import json
import numpy as np
import tensorflow as tf

storebranches = None
products = None
data_columns = None
model = None

model = tf.keras.models.load_model('myModel')

with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']
    storebranches = data_columns[1:1003]
    products = data_columns[1003:1518]

app = Flask(__name__)




def get_store_branch():
    return storebranches


def get_product_names():
    return products


@app.route('/get_store_branches', methods=['GET'])
def get_store_names():
    response = jsonify({
        'storebranches': get_store_branch()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/product', methods=['GET'])
def get_products():
    response = jsonify({
        'products': get_product_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response





@app.route('/success/<int:score>')
def success(score):
    exp = {'Total Quantity': score}
    return render_template('result.html', result=exp)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        storebranch = request.form['StoreBranch']
        product = request.form['Product']
        month = int(request.form['month'])
    try:
        storebranch_index = data_columns.index(storebranch.lower())

    except:
        storebranch_index = -1
    try:
        product_index = data_columns.index(product.lower())
    except:
        product_index = -1

    x = [0] * (len(data_columns))
    if month >= 1 and month <= 12:
        x[0] = month
    else:
        return "month should be in range 1 to 12"

    if storebranch_index >= 0:
        x[storebranch_index] = 1
    if product_index >= 0:
        x[product_index] = 1

    arr = np.array([x])
    total_score = np.argmax((model.predict([arr][0])))
    return redirect(url_for('success', score=total_score))




if __name__ == '__main__':

    app.run(debug=True)
