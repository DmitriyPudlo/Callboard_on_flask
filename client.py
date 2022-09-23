from datetime import datetime
import requests


def choose_ad(ad_id):
    ad_id = int(ad_id)
    for ad in ADS:
        if ad['ad_id'] == ad_id:
            return [ad]
    return


def choose_id_ad(user_id):
    user_id = int(user_id)
    for ad in ADS:
        if ad['user_id']['user_id'] == user_id:
            return ADS.index(ad)




now = datetime.now()

LOGIN = 'Ivan'
PASSWORD = '123'
EMAIL = 'ivan@mail.ru'
url = 'http://127.0.0.1:5000/ads/api/ads'
TITLE_AD_1 = 'Продам корову'
TEXT_AD_1 = 'Продается отличная корова. Весит 500кг, молока даёт много.'
TIME_AD_1 = now.strftime("%d-%m-%Y")

TITLE_AD_2 = 'Куплю барана'
TEXT_AD_2 = 'Хочу купить барана. Катать на нем болвана.'
TIME_AD_2 = now.strftime("%d-%m-%Y")


USERS = [{'user_id': 1,
          'login': 'Ivan',
          'email': 'ivan@mail.ru',
          'password': '123'},
         {'user_id': 2,
          'login': 'Vova',
          'email': 'vova@mail.ru',
          'password': '345'}
         ]

ADS = [{'ad_id': 1,
        'title': TITLE_AD_1,
        'text_ad': TEXT_AD_1,
        'time': TIME_AD_1,
        'user_id': USERS[0]},
       {'ad_id': 2,
        'title': TITLE_AD_2,
        'text_ad': TEXT_AD_2,
        'time': TIME_AD_2,
        'user_id': USERS[1]}
       ]

# import requests
# from Callboard import register
# url = 'http://127.0.0.1:5000/ads/api/ads'
#
# register('Ivan', 'ivan@mail.ru', '123')
# register('Vova', 'Vova@mail.ru', '3453')
#
# ad = (TITLE_AD_1, TEXT_AD_1)
#
# jsons = {'title': TITLE_AD_1, 'text_ad': TEXT_AD_1}
# jsons = {'title': TITLE_AD_2, 'text_ad': TEXT_AD_2}
#
# params = {'login': 'Ivan', 'password': '123'}
# params = {'login': 'Vova', 'password': '345'}
# params={'ad_id': 1}
# requests.post(url, json=jsons, params=params)