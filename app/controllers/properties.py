from app.models.building import Building

properties: list = [
    Building(position=1, selling_price=6, rent_price=15),
    Building(position=2, selling_price=150, rent_price=23),
    Building(position=3, selling_price=219, rent_price=37),
    Building(position=4, selling_price=312, rent_price=29),
    Building(position=5, selling_price=138, rent_price=51),
    Building(position=6, selling_price=456, rent_price=15),
    Building(position=7, selling_price=267, rent_price=15),
    Building(position=8, selling_price=377, rent_price=28),
    Building(position=9, selling_price=211, rent_price=13),
    Building(position=10, selling_price=100, rent_price=10),
    Building(position=11, selling_price=800, rent_price=80),
    Building(position=12, selling_price=483, rent_price=24),
    Building(position=13, selling_price=554, rent_price=50),
    Building(position=14, selling_price=183, rent_price=19),
    Building(position=15, selling_price=267, rent_price=25),
    Building(position=16, selling_price=393, rent_price=37),
    Building(position=17, selling_price=100, rent_price=12),
    Building(position=18, selling_price=211, rent_price=40),
    Building(position=19, selling_price=100, rent_price=13),
    Building(position=20, selling_price=300, rent_price=33)
]

board: list = [building.position for building in properties]