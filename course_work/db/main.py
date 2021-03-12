import models
from models import *


professions = models.Profession.select()

items = [
    {'company_name': 'Актива', 'company_description': 'text', 'company_number': ''},
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
    for i in Profession.select().where(Profession.profession == 'Кассир'):
        print(i.id)

print('OK...')
