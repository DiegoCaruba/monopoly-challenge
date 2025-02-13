from app.models.building import Building 

class PlayerType:

    def __init___(self, behavior: str):
        self.behavior: str = behavior
        self.cash: int = 300
        self.properties: list = []

    
    def to_pay(self, value: int) -> bool:
        self.cash -= value
        
        return (self.cash >= 0)
    

    def to_buy(self, building: Building) -> bool:
        
        if self.cash >= building.selling_price:
            self.cash -= building.selling_price
            self.properties.append(building)
            building.set_owner(self.behavior)
            return True

        return False
    
    def receive_rent(self, value:int) -> None:
        self.cash += value
