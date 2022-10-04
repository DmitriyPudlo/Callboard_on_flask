LOGIN = 'Ivan'
PASSWORD = '123'
EMAIL = 'ivan@mail.ru'
url = 'http://127.0.0.1:5000/ads/api/ads'
TITLE_AD_1 = 'Продам корову'
TEXT_AD_1 = 'Продается отличная корова. Весит 500кг, молока даёт много.'

TITLE_AD_2 = 'Куплю барана'
TEXT_AD_2 = 'Хочу купить барана. Катать на нем болвана.'


USERS = [{'user_id': 1,
          'login': 'Ivan',
          'email': 'ivan@mail.ru',
          'password': '123'},
         {'user_id': 2,
          'login': 'Vova',
          'email': 'vova@mail.ru',
          'password': '345'}
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