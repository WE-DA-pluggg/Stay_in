from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qrhfi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/main')
def info():
    return render_template('main.html')

@app.route("/info", methods=["POST"])
def hotel_post():
    hotel_list = list(db.hotel.find({}, {'_id': False}))
    count = len(hotel_list) + 1
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    title_receive = request.form['title_give']
    hotel_address_receive = request.form['hotel_address_give']

    doc = {
        'url':url_receive,
        'star':star_receive,
        'title':title_receive,
        'hotel_address':hotel_address_receive,
        'num': count
    }
    db.hotel.insert_one(doc)

    return jsonify({'msg':'등록 완료'})

@app.route("/info", methods=["GET"])
def hotel_get():
    hotel_list = list(db.hotel.find({}, {'_id': False}))
    return jsonify({'hotels': hotel_list})

@app.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user_id": payload["id"]})
        comment_receive = request.form["comment_give"]
        comment_rate = request.form["comment_rate"]
        hotel_name = request.form["hotel_name"]
        doc = {
            "nickname": user_info["nickname"],
            "hotel_name": hotel_name,
            "comment": comment_receive,
            "comment_rate": comment_rate
        }
        db.comment.insert_one(doc)
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/reviews"))


@app.route("/get_posts", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        posts = list(db.comment.find({}).limit(20))#내림차순 20개 가져오기
        for post in posts:
            post["_id"] = str(post["_id"])#고유값 이것을 항상 스트링으로 변경하기
        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.","posts":posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("/reviews"))




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)