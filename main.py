import uvicorn
from fastapi import FastAPI
from app.views.monopoly_game import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
