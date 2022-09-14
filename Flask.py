from flask import Flask, jsonify, make_response, abort, request
from datetime import datetime
import db

now = datetime.now()
DATE = now.strftime("%d-%m-%Y")
app = Flask(__name__)
database = db.Connector()


@app.route('/ads/api/ads', methods=['GET'])
def get_ads():
    ads = database.show_all()
    return jsonify(ads)


@app.route('/ads/api/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = database.show_ad_on_ad(ad_id)
    if not ad:
        abort(404)
    return jsonify(ad)


@app.route('/ads/api/ads', methods=['POST'])
def add_ad():
    if not request.json or not ('title' or 'text_ad') in request.json:
        abort(404)
    title = request.json['title']
    text_ad = request.json['text_ad']
    database.add_ad(title, text_ad, DATE, user_id)
    ad = database.show_ad_on_user(user_id)
    return jsonify(ad), 201


@app.route('/ads/api/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    ad = database.show_ad_on_ad(ad_id)
    if not ad:
        abort(404)
    database.del_ad(ad_id)
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
