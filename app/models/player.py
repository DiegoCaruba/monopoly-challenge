from app.helper.utils import flip_a_coin

from app.models.building import Building 
from app.models.player_type import PlayerType

class Player(PlayerType):

    def __init__(self, behavior: str):
        super().__init__(behavior=behavior)


    def buy_building(self, building: Building) -> bool:
        
        if self.behavior == "cauteloso":
            remaining_cash: int = self.cash - building.selling_price
            if remaining_cash >= 80:
                return self.to_buy(building=building)
            return False

        elif self.behavior == "aleatorio":
            if flip_a_coin():
                return self.to_buy(building=building)
            return False

        elif self.behavior == "exigente":
            if building.rent_price > 50:
                return self.to_buy(building=building)
            return False

        elif self.behavior == "impulsivo":
            return self.to_buy(building=building)
        