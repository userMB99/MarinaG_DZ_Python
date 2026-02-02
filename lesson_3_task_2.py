from smartphone import Smartphone

catalog = [
    Smartphone ("Samsung", "Galaxy S25 FE", "+79995554433"),
    Smartphone ("HUAWEI", "Pura 80 Pro", "+79272223344"),
    Smartphone ("HONOR", "400 Pro", "+79953336677"),
    Smartphone ("Xiaomi", "Redmi Note 14 Pro", "+79196660011"),
    Smartphone ("POCO", "F7 Ultra", "+79875550099")
] 

for smartphone in catalog:
    print(f"{smartphone.brand_phone} - {smartphone.model_phone} . {smartphone.number_phone}")
    