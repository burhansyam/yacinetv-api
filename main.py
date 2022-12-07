# by aimadnet
# contact: t.me/aimadnet

from fastapi import FastAPI

import routes

app = FastAPI(
    title="YacineTV",
    description="This is an unofficial api wrapper for yacineapp.tv in python",
    version="1.0.0",
)

app.include_router(routes.router)


@app.get("/")
async def index():
    return {"message": "Matamu Sempal!"}
