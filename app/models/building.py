class Building:

    def __init__(self, position: int, selling_price: int, rent_price: int):
        self.position: int = position 
        self.selling_price: int = selling_price 
        self.rent_price: int = rent_price
        self.owner: str = None

    
    def set_owner(self, owner: str) -> None:
        self.owner = owner
    

    def reset_owner(self) -> None:
        self.owner = None
