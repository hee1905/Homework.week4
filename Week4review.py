from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://hee1905:08dlgmlwo!@cluster0-3ojrw.mongodb.net/test?retryWrites=true&w=majority")
db = client.shoppingmall


@app.route('/')
def home():
    return render_template('shopping mall.html')


@app.route('/order', methods=['post'])
def write_orders():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    orders = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.shoppingmall.insert_one(orders)

    return jsonify({'result': 'success', 'msg': '오더가 완료 되었습니다.'})


@app.route('/order', methods=['GET'])
def read_orders():
    orders = list(db.shoppingmall.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
