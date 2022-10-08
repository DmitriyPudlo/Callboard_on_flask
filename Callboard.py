from flask import Flask, jsonify, make_response, abort, request
from datetime import datetime
import db


def register(login, email, password):
    email = email.lower()
    check = database.check_email(email)
    if not check:
        database.add_user(login, email, password)
    else:
        print('Данная почта уже используется')
    return


now = datetime.now()
DATE = now.strftime("%d-%m-%Y")
app = Flask(__name__)
database = db.Connector()


@app.route('/ads/api/ads', methods=['GET'])
def get_ads():
    ad_id = request.args.get('ad_id')
    if not ad_id:
        ads = database.show_all()
        return jsonify(ads)
    ad = database.show_ad_on_ad(ad_id)
    if not ad:
        abort(404)
    return jsonify(ad)


@app.route('/ads/api/ads', methods=['POST'])
def add_update_ad():
    login = request.args.get('login')
    password = request.args.get('password')
    title = request.args.get('title')
    text_ad = request.args.get('text_ad')
    ad_id = request.args.get('ad_id')
    if not login or not password:
        return abort(404)
    user_id = database.check_authenticated(login, password)
    if not user_id:
        return abort(404)
    if ad_id:
        if database.show_ad_on_ad(ad_id):
            database.update(ad_id, title, text_ad)
            ad = database.show_ad_on_user(user_id)
            return jsonify(ad), 201
        else:
            return abort(404)
    else:
        if not title or not text_ad:
            return abort(404)
        else:
            database.add_ad(title, text_ad, DATE, user_id)
            ad = database.show_ad_on_user(user_id)
            return jsonify(ad), 201


@app.route('/ads/api/ads', methods=['DELETE'])
def delete_ad():
    if not request.args.get('login') or not request.args.get('password'):
        return abort(404)
    ad_id = request.args.get('ad_id')
    if not ad_id:
        abort(404)
    login = request.args.get('login')
    password = request.args.get('password')
    user_id_from_params = database.check_authenticated(login, password)
    user_id_from_db = database.show_user_id_on_ad(ad_id)
    if user_id_from_params[0] == user_id_from_db[0]:
        database.del_ad(ad_id)
        return jsonify({'result': True})
    return abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
