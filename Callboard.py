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
    ad_id = int(ad_id[0])
    ad = database.show_ad_on_ad(ad_id)
    if not ad:
        abort(404)
    return jsonify(ad)


@app.route('/ads/api/ads', methods=['POST'])
def add_ad():
    if not request.args['login'] or not request.args['password']:
        return abort(404)
    login = request.args['login']
    password = request.args['password']
    user_id = database.check_authenticated(login, password)
    user_id = int(user_id[0])
    if user_id:
        if not request.json or not ('title' or 'text_ad') in request.json:
            abort(404)
        title = request.json['title']
        text_ad = request.json['text_ad']
        database.add_ad(title, text_ad, DATE, user_id)
        ad = database.show_ad_on_user(user_id)
        return jsonify(ad), 201
    return abort(404)


@app.route('/ads/api/ads', methods=['DELETE'])
def delete_ad():
    print(not request.args.get('login') or not request.args.get('password'))
    if not request.args.get('login') or not request.args.get('password'):
        return abort(404)
    ad_id = request.args.get('ad_id')
    print(not ad_id)
    if not ad_id:
        abort(404)
    ad_id = int(ad_id[0])
    login = request.args.get('login')
    password = request.args.get('password')
    user_id_from_params = database.check_authenticated(login, password)
    user_id_from_db = database.show_user_id_on_ad(ad_id)
    print(user_id_from_params[0] == user_id_from_db[0])
    if user_id_from_params[0] == user_id_from_db[0]:
        database.del_ad(ad_id)
        return jsonify({'result': True})
    return abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# from flask import Flask, jsonify, make_response, abort, request
# from client import ADS, choose_ad, choose_id_ad, USERS
# from datetime import datetime
# import db
#
# now = datetime.now()
# DATE = now.strftime("%d-%m-%Y")
# app = Flask(__name__)
# database = db.Connector()
#
#
# def register(login, email, password):
#     for user in USERS:
#         if user['email'] == email:
#             print('Данная почта уже используется')
#             return
#     new_user = {'user_id': USERS[-1]['user_id'] + 1,
#                 'login': f'{login}',
#                 'email': f'{email.lower()}',
#                 'password': f'{password}'}
#     USERS.append(new_user)
#     return
#
#
# def check_authenticated(info):
#     login = info['login']
#     password = info['password']
#     id_user = database.check_authenticated(login, password)
#     if not id_user:
#         return False
#     return True
#
# @app.route('/ads/api/ads', methods=['GET'])
# def get_ads():
#     ad_id = request.args.get('ad_id')
#     if not ad_id:
#         return jsonify(ADS)
#     ad = choose_ad(ad_id)
#     if not ad:
#         abort(404)
#     return jsonify(ad)
#
#
# @app.route('/ads/api/ads', methods=['POST'])
# def add_ad():
#     if check_authenticated(request.args):
#         if not request.json or not ('title' or 'text_ad') in request.json:
#             abort(404)
#         id_for_ad = ADS[-1]['ad_id'] + 1
#         ad = {'ad_id': id_for_ad,
#               'title': request.json['title'],
#               'text_ad': request.json['text_ad'],
#               'time': DATE,
#               'user_id': USERS[0]}
#         ADS.append(ad)
#         return jsonify(ad), 201
#     return abort(404)
#
# @app.route('/ads/api/ads', methods=['DELETE'])
# def delete_ad():
#     user_id_from_ad = request.args.get('user_id')
#     if not user_id_from_ad:
#         abort(404)
#     user_id_from_params = check_authenticated(request.args)
#     if user_id_from_params == user_id_from_ad:
#         ad_index = choose_id_ad(user_id_from_ad)
#         del ADS[ad_index]
#         return jsonify({'result': True})
#     return abort(404)
#
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)