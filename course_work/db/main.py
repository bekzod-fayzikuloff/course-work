import models
from models import *

text = '''Официальный сайт компании РЛС ®. Энциклопедия лекарств и товаров аптечного ассортимента российского интернета. Справочник лекарственных препаратов Rlsnet.ru предоставляет пользователям доступ к инструкциям, ценам и описаниям лекарственных средств, БАДов, медицинских изделий,'''

professions = models.Profession.select()

items = [
    {'company_name': 'Актива', 'company_description': text, 'company_number': ''},
    {'company_name': 'BOIRON', 'company_description': 'Смирнов', 'company_number': ''},
    {'company_name': 'Пептек', 'company_description': '', 'company_number': ''},
    {'company_name': 'Никитская лаборатория', 'company_description': '', 'company_number': ''},
    {'company_name': 'ДДД', 'company_description': '', 'company_number': ''},
    {'company_name': 'Долфин', 'company_description': '', 'company_number': ''},
    {'company_name': 'Эхо', 'company_description': '', 'company_number': ''},
    {'company_name': 'Lekinterkaps', 'company_description': '', 'company_number': ''},
    {'company_name': 'Европа-Биофарм', 'company_description': '', 'company_number': ''},
    {'company_name': 'Факел-дизайн', 'company_description': '', 'company_number': ''},
    {'company_name': 'STADA', 'company_description': '', 'company_number': ''},
    {'company_name': 'Верофарм', 'company_description': '', 'company_number': ''},
    {'company_name': 'ДиаКлон', 'company_description': '', 'company_number': ''},
]

with db:
    models.Maker.insert_many(items).execute()

print('OK...')
