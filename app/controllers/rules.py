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
        print(new_position)
        current_building: Building = list(filter(lambda obj: obj.position == new_position, self.board))
        return current_building[0]
    
    
    def get_current_owner(self, behavior: str) -> Player:
        current_owner: Player = list(filter(lambda obj: obj.behavior == behavior, self.players))
        return current_owner[0]
       

    def monopoly_simulation(self) -> None:

        for round in range(100):

            for player in self.players[:]:
                print(f"Round {round}: Player {(player.behavior).upper()}", end=" ")

                if player.cash < 0:
                    self.clear_property(player)
                    player.clear_properties()
                    self.players.remove(player)
                    print(f"has left the game")
                    continue

                if len(self.players) == 1:
                    print("fim")
                    return 'self.build_final_result()'
            
                pace = throw_dice()
                former_position: int = player.board_position
                player.set_new_board_position(pace)
                new_position: int = player.board_position
                print(f"walks {pace} paces from {former_position} to {new_position}")

                current_building: Building = self.get_current_building(new_position)

                if current_building.owner is None:
                    player.buy_building(current_building)
                elif current_building.owner != player.behavior:
                    rent_value: int = current_building.rent_price
                    owner: Player = self.get_current_owner(current_building.owner)
                    
                    player.to_pay(rent_value)
                    owner.receive_rent(rent_value)
            
            print()
