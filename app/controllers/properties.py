from random import randint
from app.models.building import Building

properties: list = [
    Building(position=1,  selling_price=randint(150, 200), rent_price=randint(15, 25)),
    Building(position=2,  selling_price=randint(150, 300), rent_price=randint(15, 65)),
    Building(position=3,  selling_price=randint(150, 500), rent_price=randint(15, 85)),
    Building(position=4,  selling_price=randint(150, 600), rent_price=randint(15, 35)),
    Building(position=5,  selling_price=randint(200, 600), rent_price=randint(45, 95)),
    Building(position=6,  selling_price=randint(100, 400), rent_price=randint(15, 25)),
    Building(position=7,  selling_price=randint(150, 200), rent_price=randint(15, 65)),
    Building(position=8,  selling_price=randint(150, 300), rent_price=randint(15, 85)),
    Building(position=9,  selling_price=randint(150, 500), rent_price=randint(15, 35)),
    Building(position=10, selling_price=randint(150, 600), rent_price=randint(45, 95)),
    Building(position=11, selling_price=randint(200, 600), rent_price=randint(15, 25)),
    Building(position=12, selling_price=randint(100, 400), rent_price=randint(15, 65)),
    Building(position=13, selling_price=randint(150, 200), rent_price=randint(15, 85)),
    Building(position=14, selling_price=randint(150, 300), rent_price=randint(15, 35)),
    Building(position=15, selling_price=randint(150, 500), rent_price=randint(45, 95)),
    Building(position=16, selling_price=randint(150, 600), rent_price=randint(15, 25)),
    Building(position=17, selling_price=randint(200, 600), rent_price=randint(15, 65)),
    Building(position=18, selling_price=randint(100, 400), rent_price=randint(15, 85)),
    Building(position=19, selling_price=randint(150, 200), rent_price=randint(15, 35)),
    Building(position=20, selling_price=randint(150, 300), rent_price=randint(45, 95))
]
