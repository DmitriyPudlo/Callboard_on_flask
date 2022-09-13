from flask import Flask, jsonify, make_response, abort, request
from client import ADS, choose_ad
from datetime import datetime

now = datetime.now()
DATE = now.strftime("%d-%m-%Y")
app = Flask(__name__)


@app.route('/ads/api/ads', methods=['GET'])
def get_ads():
    return jsonify(ADS)


@app.route('/ads/api/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = choose_ad(ad_id)
    if not ad:
        abort(404)
    return jsonify(ad)


@app.route('/ads/api/ads', methods=['POST'])
def add_ad():
    if not request.json or not ('title' or 'text_ad') in request.json:
        abort(404)
    ad = {'ad_id': ADS[-1]['ad_id'] + 1,
          'title': request.json['title'],
          'text_ad': request.json['text_ad'],
          'time': DATE,
          'user_id': ADS[-1]['user_id'] + 1}
    ADS.append(ad)
    return jsonify(ad), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
