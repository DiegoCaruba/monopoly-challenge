import random

from app.models.player import Player
from app.models.building import Building

from app.helper.utils import throw_dice

from app.controllers.properties import properties

class Rules:

    def __init__(self):
        self.players: list = [
            Player(behavior="impulsivo"),
            Player(behavior="exigente"),
            Player(behavior="cauteloso"),
            Player(behavior="aleatorio")
        ]
        # random.shuffle(self.players)
        self.board: list[Building] = properties

    
    def clear_property(self, player: Player) -> None:
        player_buildings = player.properties
        
        for building in player_buildings:
            building.reset_owner()

    
    def get_current_building(self, new_position: int) -> Building:
        current_building: Building = list(filter(lambda obj: obj.position == new_position, self.board))
        return current_building[0]
    
    
    def get_current_owner(self, behavior: str) -> Player:
        current_owner: Player = list(filter(lambda obj: obj.behavior == behavior, self.players))
        return current_owner[0]


    def build_final_result(self, winner: Player, final_result: list[Player]) -> dict:
        ordered_players: list = sorted(final_result, key=lambda x: x.cash, reverse=True)

        result: dict = {
            "vencedor": winner.behavior,
            "jogadores": [player.behavior for player in ordered_players]
        }

        print(result)
        return result


    def monopoly_simulation(self) -> None:

        final_result: list[Player] = []

        for round in range(1000):

            for player in self.players[:]:

                if player.cash < 0:
                    self.clear_property(player)
                    player.clear_properties()
                    self.players.remove(player)
                    final_result.append(player)
                    continue

                if len(self.players) == 1:

                    return self.build_final_result(self.players[0], final_result)
            
                pace = throw_dice()
                player.set_new_board_position(pace)
                new_position: int = player.board_position

                current_building: Building = self.get_current_building(new_position)

                if current_building.owner is None:
                    player.buy_building(current_building)
                elif current_building.owner != player.behavior:
                    rent_value: int = current_building.rent_price
                    owner: Player = self.get_current_owner(current_building.owner)
                    
                    player.to_pay(rent_value)
                    owner.receive_rent(rent_value)
            
