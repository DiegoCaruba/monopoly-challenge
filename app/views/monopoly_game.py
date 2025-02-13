from fastapi import APIRouter

from app.controllers.rules import Rules

router = APIRouter()

@router.get("/jogo/simular")
def get_monopoly_result():

    game: Rules = Rules()

    res = game.monopoly_simulation()

    return res