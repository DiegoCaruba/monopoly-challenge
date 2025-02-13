from app.helper.utils import flip_a_coin
from app.models.building import Building 
from app.models.player_type import PlayerType

class Player(PlayerType):

    def __init__(self):
        super().__init__()


    def buy_building(self, building: Building) -> bool:

        if self.behavior == "cauteloso":
            remaining_cash: int = building.selling_price - self.cash
            if remaining_cash >= 80:
                self.to_buy(building=building)

        elif self.behavior == "aleatorio":
            if flip_a_coin():
                self.to_buy(building=building)

        elif self.behavior == "exigente":
            if building.rent_price > 50:
                self.to_buy(building=building)

        elif self.behavior == "impulsivo":
            self.to_buy(building=building)
        
        else:
            return False