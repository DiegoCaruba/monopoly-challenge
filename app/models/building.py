class Building:

    def __init__(self, building_id: str, selling_price: int, rent_price: int):
        self.building_id: str = building_id 
        self.selling_price: int = selling_price 
        self.rent_price: int = rent_price
        self.owner: str = None

    
    def set_owner(self, owner: str) -> None:
        self.owner = owner
    

    def reset_owner(self) -> None:
        self.owner = None
