import asyncio

from fastapi import FastAPI
import uvicorn

from app.db.associative import UserTeamAssoc, Result
from app.db.teams.models import Team
from app.db.tournaments.models import Tournament
from app.db.users.models import User
from app.db.base import create_db
from app.routes.users import users_route
from app.routes.teams import teams_router
from app.routes.tournaments import tournaments_route

app = FastAPI()
app.include_router(users_route)
app.include_router(teams_router)
app.include_router(tournaments_route)

if __name__ == "__main__":
    # asyncio.run(create_db())
    uvicorn.run("main:app", reload=True)