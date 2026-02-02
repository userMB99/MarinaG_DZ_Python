from address import Address
from mailing import Mailing

to_address = Address("127427", "Москва", "Академика Королева", "15-", "1")
from_address = Address("190000", "Санкт-Петербург", "Дворцовая набережная", "дом 34", "1")
track = "45005145009749"
cost = "500"

mailing = Mailing(to_address, from_address, cost, track) 
print(f"Отправление {mailing.track} из {mailing.from_address.index} , {mailing.from_address.city},"
    f"{mailing.from_address.street} , {mailing.from_address.house} , {mailing.from_address.apartment}"
    f" в {mailing.to_address.index}, {mailing.to_address.city}," 
    f"{mailing.to_address.street}, {mailing.to_address.house}, {mailing.to_address.apartment}. " 
    f"Стоимость {mailing.cost} рублей")
