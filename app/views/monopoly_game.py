from fastapi import APIRouter

from app.helper.utils import logger
from app.controllers.rules import Rules

router = APIRouter()

@router.get("/jogo/simular")
def get_monopoly_result():

    game: Rules = Rules()

    res = game.monopoly_simulation()

    logger(f"Resultado da simulação: {res}")

    return res