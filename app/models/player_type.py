from app.models.building import Building 

class PlayerType:

    def __init__(self, behavior: str):
        self.behavior: str = behavior
        self.cash: int = 300
        self.properties: list = []
        self.board_position: int = 0

    
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

    
    def clear_properties(self) -> None:
        self.properties = []
    

    def set_new_board_position(self, pace: int) -> None:
        new_position: int = (self.board_position + pace) % 20
        self.board_position = new_position if new_position != 0 else 20